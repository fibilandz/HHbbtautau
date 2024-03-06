from analysis_tools import ObjectCollection, Category, Process, Dataset, Feature, Systematic
from analysis_tools.utils import DotDict
from analysis_tools.utils import join_root_selection as jrs
from plotting_tools import Label
from collections import OrderedDict

from cmt.config.base_config import Config as cmt_base_config
from cmt.base_tasks.base import Task

class Config(cmt_base_config):
    def __init__(self, *args, **kwargs):
        self = self.add_tau_id(2022, "idDeepTau2018v2p5")
        self = self.add_bjet_id("PNetB")
        self.channels = self.add_channels()
        self.regions = self.add_regions()
        self.categories = self.add_categories()
        super(Config, self).__init__(*args, **kwargs)

    def join_selection_channels(self, selection):
        return jrs([jrs(jrs(selection[ch.name], op="and"), ch.selection, op="and")
            for ch in self.channels], op="or")

    def combine_selections_per_channel(self, selection1, selection2):
        selection = DotDict()
        for channel in selection1:
            selection[channel] = jrs(jrs(selection1[channel], op="and"),
                jrs(selection2[channel], op="and"), op="or")
        return selection

    def add_regions(self):
        selection = OrderedDict()
        region_names = ["Signal region", "OS inv. iso", "SS iso", "SS inv. iso"]
        selection["os_iso"] = {
            "mutau":  ["isOS == 1",
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium],
            "etau":   ["isOS == 1",
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium],
            "tautau": ["isOS == 1",
                       "dau1_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium,
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium],
        }
        selection["os_inviso"] = {
            "mutau":  ["isOS == 1", 
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.VVVLoose,
                       "dau2_tauIdVSjet < %s" % self.tauId_algo_wps.vsjet.Medium],
            "etau":   ["isOS == 1",
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.VVVLoose,
                       "dau2_tauIdVSjet < %s" % self.tauId_algo_wps.vsjet.Medium],
            "tautau": ["isOS == 1",
                       "dau1_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium,
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.VVVLoose,
                       "dau2_tauIdVSjet < %s" % self.tauId_algo_wps.vsjet.Medium],
        }
        selection["ss_iso"] = {
            "mutau":  ["isOS == 0",
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium],
            "etau":   ["isOS == 0",
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium],
            "tautau": ["isOS == 0",
                       "dau1_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium,
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium],
        }
        selection["ss_inviso"] = {
            "mutau":  ["isOS == 0", 
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.VVVLoose,
                       "dau2_tauIdVSjet < %s" % self.tauId_algo_wps.vsjet.Medium],
            "etau":   ["isOS == 0",
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.VVVLoose,
                       "dau2_tauIdVSjet < %s" % self.tauId_algo_wps.vsjet.Medium],
            "tautau": ["isOS == 0",
                       "dau1_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.Medium,
                       "dau2_tauIdVSjet >= %s" % self.tauId_algo_wps.vsjet.VVVLoose,
                       "dau2_tauIdVSjet < %s" % self.tauId_algo_wps.vsjet.Medium],
        }
        regions = []
        for channel in self.channels:
            regions.append(channel)
            regions.append(
                Category(channel.name + "_os", label=channel.label,
                    selection=" (%s) && (isOS == 1)" % channel.selection)
            )
        for ikey, key in enumerate(selection):
            regions.append(Category(key, label=Label(region_names[ikey]),
                selection=self.join_selection_channels(selection[key])))
            for channel in self.channels:
                regions.append(Category("_".join([channel.name, key]),
                    label=Label(", ".join([channel.label.root + " channel", region_names[ikey]])),
                    selection=jrs(channel.selection,
                        jrs(selection[key][channel.name], op="and"), op="and")))
        return ObjectCollection(regions)

    def add_channels(self):
        channels = [
            Category("mutau", Label("#tau_{#mu}#tau_{h}"), selection="pairType == 0"),
            Category("etau", Label("#tau_{e}#tau_{h}"), selection="pairType == 1"),
            Category("tautau", Label("#tau_{h}#tau_{h}"), selection="pairType == 2"),
        ]
        return ObjectCollection(channels)

    def add_categories(self, **kwargs):
        reject_sel = ["pairType == -31415"]

        sel = DotDict()
        btag = kwargs.pop("btag", "Jet_btag%s.at(bjet{}_JetIdx)" % self.btag_algo)
        df = lambda i, op, wp: "{} {} {}".format(btag.format(i), op, self.btag_algo_wps[wp])
        sel["btag"] = DotDict(
            m_first=[df(1, ">", "medium")],
            m_second=[df(2, ">", "medium")],
            m_any=[jrs(df(1, ">", "medium"), df(2, ">", "medium"), op="or")],
            l=[df(1, ">", "loose"), df(2, "<", "loose")],
            ll=[df(1, ">", "loose"), df(2, ">", "loose")],
            m=[jrs(jrs(df(1, ">", "medium"), df(2, "<", "medium"), op="and"),
                jrs(df(1, "<", "medium"), df(2, ">", "medium"), op="and"), op="or")],
            mm=[df(1, ">", "medium"), df(2, ">", "medium")],
            not_mm=[df(1, "<", "medium"), df(2, "<", "medium")],
        )

        _excl_vbf_loose_nob = ["{{VBFjj_mass}} > 500", "abs({{VBFjj_deltaEta}}) > 3",
            "isVBFtrigger == 0"]
        _excl_vbf_loose = _excl_vbf_loose_nob + sel.btag.m_any
        _excl_non_vbf_loose = ["!" + jrs(_excl_vbf_loose, op="and")]

        _excl_vbf_tight_nob = ["{{vbfjet1_pt}} > 140", "{{vbfjet2_pt}} > 60", "{{VBFjj_mass}} > 800",
            "abs({{VBFjj_deltaEta}}) > 3", "isVBFtrigger == 1"]
        _excl_vbf_tight = _excl_vbf_tight_nob + sel.btag.m_any
        _excl_non_vbf_tight = ["!" + jrs(_excl_vbf_tight, op="and")]

        _excl_non_vbf = ["!" + jrs(jrs(_excl_vbf_loose, op="and"), jrs(_excl_vbf_tight, op="and"),
            op="or")]

        mass_ellipse_sel = ["(({{Htt_svfit_mass}} - 129.) * ({{Htt_svfit_mass}} - 129.)/ (53. * 53.)"
            " + ({{Hbb_mass}} - 169.) * ({{Hbb_mass}} - 169.) / (145. * 145.)) < 1"]
        mass_boost_sel = ["(({{Htt_svfit_mass}} - 128.) * ({{Htt_svfit_mass}} - 128.) / (60. * 60.)"
            " + ({{Hbb_mass}} - 159.) * ({{Hbb_mass}} - 159.) / (94. * 94.)) < 1"]
        sel["resolved_1b"] = DotDict({
            ch: (sel.btag.m + mass_ellipse_sel + ["isBoosted != 1"]
                + _excl_non_vbf_loose)
            for ch in self.channels.names()
        })
        sel["resolved_1b_combined"] = self.join_selection_channels(sel["resolved_1b"])
        sel["resolved_2b"] = DotDict({
            ch: (sel.btag.mm + mass_ellipse_sel + ["isBoosted != 1"]
                + _excl_non_vbf)
            for ch in self.channels.names()
        })
        sel["resolved_2b_combined"] = self.join_selection_channels(sel["resolved_2b"])
        sel["boosted"] = DotDict({
            ch: (sel.btag.ll + mass_boost_sel + ["isBoosted == 1"]
                + _excl_non_vbf)
            for ch in self.channels.names()
        })
        sel["boosted_combined"] = self.join_selection_channels(sel["boosted"])
        sel["vbf_loose"] = DotDict({
            ch: _excl_vbf_loose
            for ch in self.channels.names()
        })
        sel["vbf_loose_combined"] = self.join_selection_channels(sel.vbf_loose)
        sel["vbf_tight"] = DotDict(
            mutau=reject_sel,  # category not used, should always reject
            etau=reject_sel,  # category not used, should always reject
            tautau=_excl_vbf_tight + sel.btag.m_any,
        )
        sel["vbf_tight_combined"] = self.join_selection_channels(sel.vbf_tight)
        sel["vbf"] = self.combine_selections_per_channel(sel.vbf_tight, sel.vbf_loose)
        sel["vbf_combined"] = self.join_selection_channels(sel.vbf)

        categories = [
            Category("base", "base category", selection="event >= 0"),
            Category("baseline", "Baseline", selection="pairType >= 0 && pairType <= 2"),
            Category("base_selection", "base category",
                nt_selection="(Sum$(Tau_pt->fElements > 17) > 0"
                    " && ((Sum$(Muon_pt->fElements > 17) > 0"
                    " || Sum$(Electron_pt->fElements > 17) > 0)"
                    " || Sum$(Tau_pt->fElements > 17) > 1)"
                    " && Sum$(Jet_pt->fElements > 17) > 1)",
                selection="Tau_pt[Tau_pt > 10].size() > 0 "
                    "&& ((Muon_pt[Muon_pt > 17].size() > 0"
                    "|| Electron_pt[Electron_pt > 17].size() > 0)"
                    "|| Tau_pt[Tau_pt > 10].size() > 1)"
                    "&& Jet_pt[Jet_pt > 17].size() > 0"),
            # Category("dum", "dummy category", selection="event == 220524669"),
            Category("dum", "dummy category", selection="event == 74472670"),
            Category("mutau", "#tau_{#mu}#tau_{h} channel", selection="pairType == 0",
                skip_processes=["data_etau", "data_tau"]),
            Category("etau", "#tau_{e}#tau_{h} channel", selection="pairType == 1",
                skip_processes=["data_mutau", "data_tau"]),
            # Category("etau", "e#tau channel", selection="pairType >= -999"),
            # Category("etau", "e#tau channel", selection="1."),
            Category("tautau", "#tau_{h}#tau_{h} channel", selection="pairType == 2",
                skip_processes=["data_etau", "data_mutau"]),
            Category("resolved_1b", label="Resolved 1b category",
                selection=sel["resolved_1b_combined"]),
            Category("resolved_2b", label="Resolved 2b category",
                selection=sel["resolved_2b_combined"]),
            Category("boosted", label="Boosted category",
                selection=sel["boosted_combined"]),
            Category("vbf_loose", label="VBF (loose) category",
                selection=sel["vbf_loose_combined"]),
            Category("vbf_tight", label="VBF (tight) category",
                selection=sel["vbf_tight_combined"]),
            Category("vbf", label="VBF category",
                selection=sel["vbf_combined"]),
        ]
        return ObjectCollection(categories)

    def add_processes(self):
        processes = [
            Process("data", Label("data"), color=(0, 0, 0), isData=True),
            Process("Tau_2022B", Label("Tau_2022B"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("Tau_2022C", Label("Tau_2022C"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("Tau_2022D", Label("Tau_2022D"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("SingleMuon_2022B", Label("SingleMuon_2022B"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("SingleMuon_2022C", Label("SingleMuon_2022C"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("Muon_2022D", Label("Muon_2022D"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("EGamma_2022B", Label("EGamma_2022B"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("EGamma_2022C", Label("EGamma_2022C"), color=(0, 0, 0), parent_process="data", isData=True),
            Process("EGamma_2022D", Label("EGamma_2022D"), color=(0, 0, 0), parent_process="data", isData=True),

            Process("dy", Label("dy"), color=(122, 33, 221)),
            Process("DYto2L-2Jets_MLL-10to50", Label("DYto2L-2Jets_MLL-10to50"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-10to50_ext1", Label("DYto2L-2Jets_MLL-10to50_ext1"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50", Label("DYto2L-2Jets_MLL-50"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_ext1", Label("DYto2L-2Jets_MLL-50_ext1"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_0J", Label("DYto2L-2Jets_MLL-50_0J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_1J", Label("DYto2L-2Jets_MLL-50_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_2J", Label("DYto2L-2Jets_MLL-50_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-40to100_1J", Label("DYto2L-2Jets_MLL-50_PTLL-40to100_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-40to100_2J", Label("DYto2L-2Jets_MLL-50_PTLL-40to100_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-100to200_1J", Label("DYto2L-2Jets_MLL-50_PTLL-100to200_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-100to200_2J", Label("DYto2L-2Jets_MLL-50_PTLL-100to200_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-200to400_1J", Label("DYto2L-2Jets_MLL-50_PTLL-200to400_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-200to400_2J", Label("DYto2L-2Jets_MLL-50_PTLL-200to400_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-400to600_1J", Label("DYto2L-2Jets_MLL-50_PTLL-400to600_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-400to600_2J", Label("DYto2L-2Jets_MLL-50_PTLL-400to600_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-600_1J", Label("DYto2L-2Jets_MLL-50_PTLL-600_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-2Jets_MLL-50_PTLL-600_2J", Label("DYto2L-2Jets_MLL-50_PTLL-600_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-10to50", Label("DYto2L-4Jets_MLL-10to50"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-50", Label("DYto2L-4Jets_MLL-50"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-50_ext1", Label("DYto2L-4Jets_MLL-50_ext1"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-50_1J", Label("DYto2L-4Jets_MLL-50_1J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-50_2J", Label("DYto2L-4Jets_MLL-50_2J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-50_3J", Label("DYto2L-4Jets_MLL-50_3J"), color=(122, 33, 221), parent_process="dy"),
            Process("DYto2L-4Jets_MLL-50_4J", Label("DYto2L-4Jets_MLL-50_4J"), color=(122, 33, 221), parent_process="dy"),

            Process("others", Label("others"), color=(156, 156, 161)),
            Process("WWto2L2Nu", Label("WWto2L2Nu"), color=(156, 156, 161), parent_process="others"),
            Process("WWto2L2Nu_ext1", Label("WWto2L2Nu_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("WWtoLNu2Q", Label("WWtoLNu2Q"), color=(156, 156, 161), parent_process="others"),
            Process("WWtoLNu2Q_ext1", Label("WWtoLNu2Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("WWto4Q", Label("WWto4Q"), color=(156, 156, 161), parent_process="others"),
            Process("WWto4Q_ext1", Label("WWto4Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto2L2Nu", Label("ZZto2L2Nu"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto2L2Nu_ext1", Label("ZZto2L2Nu_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto2L2Q", Label("ZZto2L2Q"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto2L2Q_ext1", Label("ZZto2L2Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto2Nu2Q", Label("ZZto2Nu2Q"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto2Nu2Q_ext1", Label("ZZto2Nu2Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto4L", Label("ZZto4L"), color=(156, 156, 161), parent_process="others"),
            Process("ZZto4L_ext1", Label("ZZto4L_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("WWW", Label("WWW"), color=(156, 156, 161), parent_process="others"),
            Process("WWZ", Label("WWZ"), color=(156, 156, 161), parent_process="others"),
            Process("WZZ", Label("WZZ"), color=(156, 156, 161), parent_process="others"),
            Process("ZZZ", Label("ZZZ"), color=(156, 156, 161), parent_process="others"),
            Process("TWminusto2L2Nu", Label("TWminusto2L2Nu"), color=(156, 156, 161), parent_process="others"),
            Process("TWminusto2L2Nu_ext1", Label("TWminusto2L2Nu_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("TWminustoLNu2Q", Label("TWminustoLNu2Q"), color=(156, 156, 161), parent_process="others"),
            Process("TWminustoLNu2Q_ext1", Label("TWminustoLNu2Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("TWminusto4Q", Label("TWminusto4Q"), color=(156, 156, 161), parent_process="others"),
            Process("TWminusto4Q_ext1", Label("TWminusto4Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("TbarWplusto2L2Nu", Label("TbarWplusto2L2Nu"), color=(156, 156, 161), parent_process="others"),
            Process("TbarWplusto2L2Nu_ext1", Label("TbarWplusto2L2Nu_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("TbarWplustoLNu2Q", Label("TbarWplustoLNu2Q"), color=(156, 156, 161), parent_process="others"),
            Process("TbarWplustoLNu2Q_ext1", Label("TbarWplustoLNu2Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("TbarWplusto4Q", Label("TbarWplusto4Q"), color=(156, 156, 161), parent_process="others"),
            Process("TbarWplusto4Q_ext1", Label("TbarWplusto4Q_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("TBbarQ_t-channel", Label("TBbarQ_t-channel"), color=(156, 156, 161), parent_process="others"),
            Process("TbarBQ_t-channel", Label("TbarBQ_t-channel"), color=(156, 156, 161), parent_process="others"),
            Process("TBbartoLplusNuBbar-s-channel", Label("TBbartoLplusNuBbar-s-channel"), color=(156, 156, 161), parent_process="others"),
            Process("TbarBtoLminusNuB-s-channel", Label("TbarBtoLminusNuB-s-channel"), color=(156, 156, 161), parent_process="others"),
            Process("TTHto2B", Label("TTHto2B"), color=(156, 156, 161), parent_process="others"),
            Process("TTHtoNon2B", Label("TTHtoNon2B"), color=(156, 156, 161), parent_process="others"),
            Process("TTWH", Label("TTWH"), color=(156, 156, 161), parent_process="others"),
            Process("TTWW", Label("TTWW"), color=(156, 156, 161), parent_process="others"),
            Process("TTZH", Label("TTZH"), color=(156, 156, 161), parent_process="others"),
            Process("TTZZ", Label("TTZZ"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets", Label("WtoLNu-2Jets"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_1J", Label("WtoLNu-2Jets_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_2J", Label("WtoLNu-2Jets_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-40to100_1J", Label("WtoLNu-2Jets_PTLNu-40to100_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-40to100_2J", Label("WtoLNu-2Jets_PTLNu-40to100_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-100to200_1J", Label("WtoLNu-2Jets_PTLNu-100to200_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-100to200_2J", Label("WtoLNu-2Jets_PTLNu-100to200_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-200to400_1J", Label("WtoLNu-2Jets_PTLNu-200to400_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-200to400_2J", Label("WtoLNu-2Jets_PTLNu-200to400_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-400to600_1J", Label("WtoLNu-2Jets_PTLNu-400to600_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-400to600_2J", Label("WtoLNu-2Jets_PTLNu-400to600_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-600_1J", Label("WtoLNu-2Jets_PTLNu-600_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-2Jets_PTLNu-600_2J", Label("WtoLNu-2Jets_PTLNu-600_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-4Jets", Label("WtoLNu-4Jets"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-4Jets_ext1", Label("WtoLNu-4Jets_ext1"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-4Jets_1J", Label("WtoLNu-4Jets_1J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-4Jets_2J", Label("WtoLNu-4Jets_2J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-4Jets_3J", Label("WtoLNu-4Jets_3J"), color=(156, 156, 161), parent_process="others"),
            Process("WtoLNu-4Jets_4J", Label("WtoLNu-4Jets_4J"), color=(156, 156, 161), parent_process="others"),

            Process("singleh", Label("singleh"), color=(248, 156, 32)),
            Process("GluGluHToTauTau", Label("GluGluHToTauTau"), color=(248, 156, 32), parent_process="singleh"),
            Process("GluGluHto2B", Label("GluGluHto2B"), color=(248, 156, 32), parent_process="singleh"),
            Process("VBFHToTauTau", Label("VBFHToTauTau"), color=(248, 156, 32), parent_process="singleh"),
            Process("VBFHto2B", Label("VBFHto2B"), color=(248, 156, 32), parent_process="singleh"),
            Process("ZH_Hto2B_Zto2L", Label("ZH_Hto2B_Zto2L"), color=(248, 156, 32), parent_process="singleh"),
            Process("ZH_Hto2B_Zto2L_ext1", Label("ZH_Hto2B_Zto2L_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("ZH_Hto2B_Zto2Q", Label("ZH_Hto2B_Zto2Q"), color=(248, 156, 32), parent_process="singleh"),
            Process("ZH_Hto2B_Zto2Q_ext1", Label("ZH_Hto2B_Zto2Q_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("WminusH_Hto2B_Wto2Q", Label("WminusH_Hto2B_Wto2Q"), color=(248, 156, 32), parent_process="singleh"),
            Process("WminusH_Hto2B_Wto2Q_ext1", Label("WminusH_Hto2B_Wto2Q_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("WminusH_Hto2B_WtoLNu", Label("WminusH_Hto2B_WtoLNu"), color=(248, 156, 32), parent_process="singleh"),
            Process("WminusH_Hto2B_WtoLNu_ext1", Label("WminusH_Hto2B_WtoLNu_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("WplusH_Hto2B_Wto2Q", Label("WplusH_Hto2B_Wto2Q"), color=(248, 156, 32), parent_process="singleh"),
            Process("WplusH_Hto2B_Wto2Q_ext1", Label("WplusH_Hto2B_Wto2Q_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("WplusH_Hto2B_WtoLNu", Label("WplusH_Hto2B_WtoLNu"), color=(248, 156, 32), parent_process="singleh"),
            Process("WplusH_Hto2B_WtoLNu_ext1", Label("WplusH_Hto2B_WtoLNu_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("ggZH_Hto2B_Zto2L", Label("ggZH_Hto2B_Zto2L"), color=(248, 156, 32), parent_process="singleh"),
            Process("ggZH_Hto2B_Zto2L_ext1", Label("ggZH_Hto2B_Zto2L_ext1"), color=(248, 156, 32), parent_process="singleh"),
            Process("ggZH_Hto2B_Zto2Q", Label("ggZH_Hto2B_Zto2Q"), color=(248, 156, 32), parent_process="singleh"),
            Process("ggZH_Hto2B_Zto2Q_ext1", Label("ggZH_Hto2B_Zto2Q_ext1"), color=(248, 156, 32), parent_process="singleh"),

            Process("ttbar", Label("ttbar"), color=(228, 37, 54)),
            Process("TTto2L2Nu", Label("TTto2L2Nu"), color=(228, 37, 54), parent_process="ttbar"),
            Process("TTto2L2Nu_ext1", Label("TTto2L2Nu_ext1"), color=(228, 37, 54), parent_process="ttbar"),
            Process("TTtoLNu2Q", Label("TTtoLNu2Q"), color=(228, 37, 54), parent_process="ttbar"),
            Process("TTtoLNu2Q_ext1", Label("TTtoLNu2Q_ext1"), color=(228, 37, 54), parent_process="ttbar"),
            Process("TTto4Q", Label("TTto4Q"), color=(228, 37, 54), parent_process="ttbar"),
            Process("TTto4Q_ext1", Label("TTto4Q_ext1"), color=(228, 37, 54), parent_process="ttbar"),

            Process("qqhh", Label("qqhh"), color=(87, 144, 252)),
            Process("VBFHHto2B2Tau_CV-1_C2V-1_C3-1", Label("VBFHHto2B2Tau_CV-1_C2V-1_C3-1"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-1_C2V-1_C3-2", Label("VBFHHto2B2Tau_CV-1_C2V-1_C3-2"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-1_C2V-2_C3-1", Label("VBFHHto2B2Tau_CV-1_C2V-2_C3-1"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4", Label("VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2", Label("VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3", Label("VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43", Label("VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94", Label("VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36", Label("VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39", Label("VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),
            Process("VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96", Label("VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96"), color=(87, 144, 252), parent_process="qqhh", isSignal=True),

            Process("gghh", Label("gghh"), color=(0, 0, 0)),
            Process("GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00", Label("GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00", Label("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00", Label("GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00", Label("GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00", Label("GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10", Label("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35", Label("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00", Label("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
            Process("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00", Label("GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00"), color=(0, 0, 0), parent_process="gghh", isSignal=True),
        ]

        process_group_names = {
            "default": [
                # "ggf_sm",
                # "data_tau",
                # "dy_high",
                # "tt_dl",
                "data",
                "dy",
                "tt",
                "others"
            ],
            "main": [
                # "ggf_sm",
                # "data_tau",
                # "dy_high",
                # "tt_dl",
                "dy",
                "tt",
                "ggf_sm",
                "vbf_sm",
            ],
            "test": [
                "ggf_sm",
                "dy",
                "tt_dl",
                "tt_sl",
            ],
            "data_tau": [
                "data_tau",
            ],
            "data_etau": [
                "data_etau",
            ],
            "bkg": [
                "tt_dl",
            ],
            "signal": [
                "ggf_sm",
            ],
            "etau": [
                "tt_dl",
                "tt_sl",
                "tt_fh",
                "dy",
                "others",
                "data_etau",
            ],
            "mutau": [
                "tt_dl",
                "tt_sl",
                "tt_fh",
                "dy",
                "others",
                "data_mutau",
            ],
            "mutau_wjets": [
                "tt_dl",
                "tt_sl",
                "tt_fh",
                "dy",
                "wjets",
                "data_mutau",
            ],
            "tautau": [
                "tt_dl",
                "tt_sl",
                "tt_fh",
                "dy",
                "others",
                "data_tau",
            ],
            "vbf": [
                "vbf_sm",
                "vbf_0p5_1_1",
                "vbf_1p5_1_1",
                "vbf_1_0_1",
                "vbf_1_1_0",
                "vbf_1_1_2",
                "vbf_1_2_1"
            ],
            "ggf": [
                "ggf_sm",
                "ggf_0_1",
                "ggf_2p45_1",
                "ggf_5_1",
            ]
        }

        process_training_names = {
            "default": [
                "ggf_sm",
                "dy"
            ]
        }

        return ObjectCollection(processes), process_group_names, process_training_names

    def add_features(self):
        features = [
            Feature("jet_pt", "Jet_pt",
                        binning=(10, 50, 150),
                        x_title=Label("jet p_{T}"),
                        units="GeV"),

            # bjet features
            Feature("bjet1_pt", "Jet_pt.at(bjet1_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("b_{1} p_{T}"),
                        units="GeV",
                        central="jet_smearing"),
            Feature("bjet1_pt_eta2p1", "Jet_pt.at(bjet1_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("b_{1} p_{T}"),
                        units="GeV",
                        selection="abs({{bjet1_eta}}) < 2.1",
                        central="jet_smearing"),
            Feature("bjet1_eta", "Jet_eta.at(bjet1_JetIdx)",
                        binning=(20, -5., 5.),
                        x_title=Label("b_{1} #eta")),
            Feature("bjet1_phi", "Jet_phi.at(bjet1_JetIdx)",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("b_{1} #phi")),
            Feature("bjet1_mass", "Jet_mass.at(bjet1_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("b_{1} m"),
                        units="GeV",
                        central="jet_smearing"),
            Feature("bjet2_pt", "Jet_pt.at(bjet2_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("b_{2} p_{T}"),
                        units="GeV",
                        central="jet_smearing"),
            Feature("bjet2_eta", "Jet_eta.at(bjet2_JetIdx)",
                        binning=(20, -5., 5.),
                        x_title=Label("b_{2} #eta")),
            Feature("bjet2_phi", "Jet_phi.at(bjet2_JetIdx)",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("b_{2} #phi")),
            Feature("bjet2_mass", "Jet_mass.at(bjet2_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("b_{2} m"),
                        units="GeV",
                        central="jet_smearing"),

            Feature("ctjet1_pt", "Jet_pt.at(ctjet_indexes.at(0))",
                        binning=(10, 50, 150),
                        x_title=Label("add. central jet 1 p_{t}"),
                        units="GeV",
                        central="jet_smearing",
                        selection="ctjet_indexes.size() > 0"),
            Feature("ctjet1_eta", "Jet_eta.at(ctjet_indexes.at(0))",
                        binning=(20, -5., 5.),
                        x_title=Label("add. central jet 1 #eta"),
                        selection="ctjet_indexes.size() > 0"),
            Feature("ctjet1_phi", "Jet_phi.at(ctjet_indexes.at(0))",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("add. central jet 1 #phi"),
                        selection="ctjet_indexes.size() > 0"),
            Feature("ctjet1_mass", "Jet_mass.at(ctjet_indexes.at(0))",
                        binning=(10, 50, 150),
                        x_title=Label("add. central jet 1 m"),
                        units="GeV",
                        central="jet_smearing",
                        selection="ctjet_indexes.size() > 0"),
            Feature("fwjet1_pt", "Jet_pt.at(fwjet_indexes.at(0))",
                        binning=(10, 50, 150),
                        x_title=Label("add. forward jet 1 p_t"),
                        units="GeV",
                        central="jet_smearing",
                        selection="fwjet_indexes.size() > 0"),
            Feature("fwjet1_eta", "Jet_eta.at(fwjet_indexes.at(0))",
                        binning=(20, -5., 5.),
                        x_title=Label("add. forward jet 1 #eta"),
                        selection="fwjet_indexes.size() > 0"),
            Feature("fwjet1_phi", "Jet_phi.at(fwjet_indexes.at(0))",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("add. forward jet 1  #phi"),
                        selection="fwjet_indexes.size() > 0"),
            Feature("fwjet1_mass", "Jet_mass.at(fwjet_indexes.at(0))",
                        binning=(10, 50, 150),
                        x_title=Label("add. forward jet 1  m"),
                        units="GeV",
                        central="jet_smearing",
                        selection="fwjet_indexes.size() > 0"),

            Feature("bjet_difpt", "abs({{bjet1_pt}} - {{bjet2_pt}})",
                        binning=(10, 50, 150),
                        x_title=Label("bb #Delta p_t"),
                        units="GeV",
                        central="jet_smearing"),

            # lepton features
             Feature("tau_pt", "Tau_pt",
                        binning=(75, 0, 150),
                        x_title=Label("#tau p_{t}"),
                        units="GeV"),
            Feature("tau_pt_tes", "Tau_pt_corr",
                        binning=(75, 0, 150),
                        x_title=Label("#tau p_{t}"),
                        units="GeV"),
            Feature("tau_mass", "Tau_mass",
                        binning=(52, 0.2, 1.5),
                        x_title=Label("#tau m"),
                        units="GeV"),
            Feature("tau_mass_tes", "Tau_mass_corr",
                        binning=(52, 0.2, 1.5),
                        x_title=Label("#tau m"),
                        units="GeV"),

            Feature("lep1_pt", "dau1_pt",
                        binning=(10, 50, 150),
                        x_title=Label("#tau_{1} p_{t}"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("lep1_eta", "dau1_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("#tau_{1} #eta")),
            Feature("lep1_phi", "dau1_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("#tau_{1} #phi")),
            Feature("lep1_mass", "dau1_mass",
                        binning=(10, 50, 150),
                        x_title=Label("#tau_{1} m"),
                        units="GeV",
                        systematics=["tes"]),

            Feature("lep2_pt", "dau2_pt",
                        binning=(10, 50, 150),
                        x_title=Label("#tau_{2} p_{t}"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("lep2_eta", "dau2_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("#tau_{2} #eta")),
            Feature("lep2_phi", "dau2_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("#tau_{2} #phi")),
            Feature("lep2_mass", "dau2_mass",
                        binning=(10, 50, 150),
                        x_title=Label("#tau_{2} m"),
                        units="GeV",
                        systematics=["tes"]),

            # MET
            Feature("met_pt", "MET_pt",
                        binning=(10, 50, 150),
                        x_title=Label("MET p_t"),
                        units="GeV",
                        central="met_smearing"),
            Feature("met_phi", "MET_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("MET #phi"),
                        central="met_smearing"),

            # Hbb
            Feature("Hbb_pt", "Hbb_pt",
                        binning=(10, 50, 150),
                        x_title=Label("H(b #bar{b}) p_t"),
                        units="GeV"),
            Feature("Hbb_eta", "Hbb_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("H(b #bar{b}) #eta")),
            Feature("Hbb_phi", "Hbb_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("H(b #bar{b}) #phi")),
            Feature("Hbb_mass", "Hbb_mass",
                        binning=(30, 0, 300),
                        x_title=Label("H(b #bar{b}) m"),
                        units="GeV"),

            # Htt
            Feature("Htt_pt", "Htt_pt",
                        binning=(10, 50, 150),
                        x_title=Label("H(#tau^{+} #tau^{-}) p_t"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("Htt_eta", "Htt_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("H(#tau^{+} #tau^{-}) #eta"),
                        systematics=["tes"]),
            Feature("Htt_phi", "Htt_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("H(#tau^{+} #tau^{-}) #phi"),
                        systematics=["tes"]),
            Feature("Htt_mass", "Htt_mass",
                        binning=(30, 0, 300),
                        x_title=Label("H(#tau^{+} #tau^{-}) m"),
                        units="GeV"),
                #systematics=["tes"]),

            # Htt (SVFit)
            Feature("Htt_svfit_pt", "Htt_svfit_pt",
                        binning=(10, 50, 150),
                        x_title=Label("H(#tau^{+} #tau^{-}) p_t (SVFit)"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("Htt_svfit_eta", "Htt_svfit_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("H(#tau^{+} #tau^{-}) #eta (SVFit)"),
                        systematics=["tes"]),
            Feature("Htt_svfit_phi", "Htt_svfit_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("H(#tau^{+} #tau^{-}) #phi (SVFit)"),
                        systematics=["tes"]),
            Feature("Htt_svfit_mass", "Htt_svfit_mass",
                        binning=(30, 0, 300),
                        x_title=Label("H(#tau^{+} #tau^{-}) m (SVFit)"),
                        units="GeV",
                        systematics=["tes"]),

            # HH
            Feature("HH_pt", "HH_pt",
                        binning=(10, 50, 150),
                        x_title=Label("HH p_t"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("HH_eta", "HH_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("HH #eta"),
                        systematics=["tes"]),
            Feature("HH_phi", "HH_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("HH #phi"),
                        systematics=["tes"]),
            Feature("HH_mass", "HH_mass",
                        binning=(50, 0, 1000),
                        x_title=Label("HH m"),
                        units="GeV",
                        systematics=["tes"]),

            # HH (SVFit)
            Feature("HH_svfit_pt", "HH_svfit_pt",
                        binning=(10, 50, 150),
                        x_title=Label("HH p_t (SVFit)"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("HH_svfit_eta", "HH_svfit_eta",
                        binning=(20, -5., 5.),
                        x_title=Label("HH #eta (SVFit)")),
                        #systematics=["tes"]),
            Feature("HH_svfit_phi", "HH_svfit_phi",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("HH #phi (SVFit)")),
                        #systematics=["tes"]),
            Feature("HH_svfit_mass", "HH_svfit_mass",
                        binning=(50, 0, 1000),
                        x_title=Label("HH m (SVFit)"),
                        units="GeV"),
                        #systematics=["tes"]),

            # HH KinFit
            Feature("HHKinFit_mass", "HHKinFit_mass",
                        binning=(50, 0, 1000),
                        x_title=Label("HH m (Kin. Fit)"),
                        units="GeV",
                        systematics=["tes"]),
            Feature("HHKinFit_chi2", "HHKinFit_chi2",
                        binning=(30, 0, 10),
                        x_title=Label("HH #chi^2 (Kin. Fit)"),
                        systematics=["tes"]),

            # VBFjet features
            Feature("vbfjet1_pt", "Jet_pt.at(VBFjet1_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("VBFjet1 p_{t}"),
                        units="GeV",
                        central="jet_smearing"),
            Feature("vbfjet1_eta", "Jet_eta.at(VBFjet1_JetIdx)",
                        binning=(20, -5., 5.),
                        x_title=Label("VBFjet1 #eta")),
            Feature("vbfjet1_phi", "Jet_phi.at(VBFjet1_JetIdx)",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("VBFjet1 #phi")),
            Feature("vbfjet1_mass", "Jet_mass.at(VBFjet1_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("VBFjet1 m"),
                        units="GeV",
                        central="jet_smearing"),
            Feature("vbfjet2_pt", "Jet_pt.at(VBFjet2_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("VBFjet2 p_t"),
                        units="GeV",
                        central="jet_smearing"),
            Feature("vbfjet2_eta", "Jet_eta.at(VBFjet2_JetIdx)",
                        binning=(20, -5., 5.),
                        x_title=Label("VBFjet2 #eta")),
            Feature("vbfjet2_phi", "Jet_phi.at(VBFjet2_JetIdx)",
                        binning=(20, -3.2, 3.2),
                        x_title=Label("VBFjet2 #phi")),
            Feature("vbfjet2_mass", "Jet_mass.at(VBFjet2_JetIdx)",
                        binning=(10, 50, 150),
                        x_title=Label("VBFjet2 m"),
                        units="GeV",
                        central="jet_smearing"),

            # VBFjj
            Feature("VBFjj_mass", "VBFjj_mass",
                        binning=(40, 0, 1000),
                        x_title=Label("VBFjj mass"),
                        units="GeV"),
            Feature("VBFjj_deltaEta", "VBFjj_deltaEta",
                        binning=(40, -8, 8),
                        x_title=Label("#Delta#eta(VBFjj)")),
            Feature("VBFjj_deltaPhi", "VBFjj_deltaPhi",
                        binning=(40, -6.4, 6.4),
                        x_title=Label("#Delta#phi(VBFjj)")),

            # Weights
            Feature("genWeight", "genWeight",
                        binning=(20, 0, 2),
                        x_title=Label("genWeight")),
            Feature("puWeight", "puWeight",
                        binning=(20, 0, 2),
                        x_title=Label("puWeight"),
                        systematics=["pu"]),
            Feature("prescaleWeight", "prescaleWeight",
                        binning=(20, 0, 2),
                        x_title=Label("prescaleWeight")),
            Feature("trigSF", "trigSF",
                        binning=(20, 0, 2),
                        x_title=Label("trigSF")),
            Feature("L1PreFiringWeight", "L1PreFiringWeight",
                        binning=(20, 0, 2),
                        x_title=Label("L1PreFiringWeight"),
                        central="prefiring",
                        systematics=["prefiring_syst"]),
            Feature("PUjetID_SF", "PUjetID_SF",
                        binning=(20, 0, 2),
                        x_title=Label("PUjetID_SF")),

            Feature("genHH_mass", "genHH_mass",
                        binning=(100, 0, 2500),
                        x_title=Label("generator HH mass"),
                        units="GeV"),

        ]
        return ObjectCollection(features)

    def add_weights(self):
        weights = DotDict()
        weights.default = "1"

        return weights

    def add_systematics(self):
        systematics = []
        #     Systematic("tes", "_corr",
        #         affected_categories=self.categories.names(),
        #         module_syst_type="tau_syst"),
        # ]
        
        # systematics = [
        #     Systematic("jet_smearing", "_nom"),
        #     Systematic("met_smearing", ("MET", "MET_smeared")),
        #     Systematic("prefiring", "_Nom"),
        #     Systematic("prefiring_syst", "", up="_Up", down="_Dn"),
        #     Systematic("pu", "", up="Up", down="Down"),
        #     Systematic("empty", "", up="", down="")
        # ]

        return ObjectCollection(systematics)

    # other methods

    def get_channel_from_region(self, region):
        for sign in ["os", "ss"]:
            if sign in region.name:
                if region.name.startswith(sign):
                    return ""
                return region.name[:region.name.index("_%s" % sign)]
        return ""

    def get_qcd_regions(self, region, category, wp="", shape_region="os_inviso",
            signal_region_wp="os_iso", sym=False):
        # the region must be set and tagged os_iso
        if not region:
            raise Exception("region must not be empty")
        # if not region.has_tag("qcd_os_iso"):
        #     raise Exception("region must be tagged as 'qcd_os_iso' but isn't")

        # the category must be compatible with the estimation technique
        # if category.has_tag("qcd_incompatible"):
        #     raise Exception("category '{}' incompatible with QCD estimation".format(category.name))

        if wp != "":
            wp = "__" + wp

        # get other qcd regions
        prefix = region.name[:-len(signal_region_wp)]
        qcd_regions = {"ss_inviso": self.regions.get(prefix + "ss_inviso" + wp)}
        # for the inverted regions, allow different working points
        default_config = ["os_inviso", "ss_iso"]
        for key in default_config:
            region_name = (prefix + key + wp if key != "ss_iso"
                else prefix + "ss_" + signal_region_wp[len("os_"):])
            qcd_regions[key] = self.regions.get(region_name)

        if sym:
            qcd_regions["shape1"] = self.regions.get(prefix + shape_region + wp)
            qcd_regions["shape2"] = self.regions.get(
                prefix + "ss_" + signal_region_wp[len("os_"):])
        else:
            if shape_region == "os_inviso":
                qcd_regions["shape"] = self.regions.get(prefix + shape_region + wp)
            else:
                qcd_regions["shape"] = self.regions.get(
                    prefix + "ss_" + signal_region_wp[len("os_"):])
        return DotDict(qcd_regions)

    def get_norm_systematics(self, processes_datasets, region):
        """
        Method to extract all normalization systematics from the KLUB files.
        It considers the processes given by the process_group_name and their parents.
        """
        # systematics
        systematics = {}
        all_signal_names = []
        all_background_names = []
        for p in self.processes:
            if p.isSignal:
                all_signal_names.append(p.get_aux("llr_name")
                    if p.get_aux("llr_name", None) else p.name)
            elif not p.isData:
                all_background_names.append(p.get_aux("llr_name")
                    if p.get_aux("llr_name", None) else p.name)

        from cmt.analysis.systReader import systReader
        syst_folder = "files/systematics/"
        syst = systReader(Task.retrieve_file(self, syst_folder + "systematics_{}.cfg".format(
            self.year)), all_signal_names, all_background_names, None)
        syst.writeOutput(False)
        syst.verbose(False)

        channel = self.get_channel_from_region(region)
        if(channel == "mutau"):
            syst.addSystFile(Task.retrieve_file(self, syst_folder
                + "systematics_mutau_%s.cfg" % self.year))
        elif(channel == "etau"):
            syst.addSystFile(Task.retrieve_file(self, syst_folder
                + "systematics_etau_%s.cfg" % self.year))
        syst.addSystFile(Task.retrieve_file(self, syst_folder + "syst_th.cfg"))
        syst.writeSystematics()
        for isy, syst_name in enumerate(syst.SystNames):
            if "CMS_scale_t" in syst.SystNames[isy] or "CMS_scale_j" in syst.SystNames[isy]:
                continue
            for process in processes_datasets:
                original_process = process
                while True:
                    process_name = (process.get_aux("llr_name")
                        if process.get_aux("llr_name", None) else process.name)
                    if process_name in syst.SystProcesses[isy]:
                        iproc = syst.SystProcesses[isy].index(process_name)
                        systVal = syst.SystValues[isy][iproc]
                        if syst_name not in systematics:
                            systematics[syst_name] = {}
                        systematics[syst_name][original_process.name] = eval(systVal)
                        break
                    elif process.parent_process:
                        process=self.processes.get(process.parent_process)
                    else:
                        break
        return systematics


config = Config("Config", year=2022, ecm=13.6, lumi_pb=9739)
