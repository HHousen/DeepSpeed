from .replace_module import replace_transformer_layer, revert_transformer_layer
from .module_quantize import quantize_transformer_layer
from .replace_policy import DSPolicy, HFBertLayerPolicy
from .replace_module import LinearAllreduce, LinearLayer, GatherEmbedding, Normalize, ReplaceWithTensorSlicing
