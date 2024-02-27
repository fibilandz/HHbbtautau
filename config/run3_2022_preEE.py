from analysis_tools import ObjectCollection, Category, Process, Dataset, Feature, Systematic
from analysis_tools.utils import DotDict
from analysis_tools.utils import join_root_selection as jrs
from plotting_tools import Label
from collections import OrderedDict

from config.run3_base_config import Config as base_config
from config.run3_dataset_2022_preEE import Datasets_2022_preEE as dataset_config

class Config_2022_preEE(base_config, dataset_config):
    def __init__(self, *args, **kwargs):
        super(Config_2022_preEE, self).__init__(*args, **kwargs)

    def add_weights(self):
        weights = DotDict()
        weights.default = "1"
        weights.total_events_weights = ["genWeight", "puWeight"]

        # weights.mutau = ["genWeight", "puWeight", "prescaleWeight", "trigSF",
        #     "idAndIsoAndFakeSF", "L1PreFiringWeight", "PUjetID_SF",
        #     "bTagweightReshape"]

        # weights.etau = weights.mutau
        # weights.tautau = weights.mutau
        # weights.base_selection = weights.mutau
        # weights.base = weights.mutau

        # weights.channels_mult = {channel: jrs(weights.channels[channel], op="*")
            # for channel in weights.channels}
        return weights

    def add_default_module_files(self):
        defaults = {}
        defaults["PreprocessRDF"] = "run3_modulesrdf"
        defaults["PreCounter"] = "run3_weights"
        return defaults


config = Config_2022_preEE("Config_2022_preEE", year=2022, ecm=13.6, lumi_pb=9739)