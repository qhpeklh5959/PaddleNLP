# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
# Copyright 2022 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa

from . import DummyObject, requires_backends


class FastDeployStableDiffusionImg2ImgPipeline(metaclass=DummyObject):
    _backends = ["paddle", "paddlenlp", "fastdeploy"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])


class FastDeployStableDiffusionInpaintPipeline(metaclass=DummyObject):
    _backends = ["paddle", "paddlenlp", "fastdeploy"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])


class FastDeployStableDiffusionInpaintPipelineLegacy(metaclass=DummyObject):
    _backends = ["paddle", "paddlenlp", "fastdeploy"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])


class FastDeployStableDiffusionMegaPipeline(metaclass=DummyObject):
    _backends = ["paddle", "paddlenlp", "fastdeploy"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])


class FastDeployStableDiffusionPipeline(metaclass=DummyObject):
    _backends = ["paddle", "paddlenlp", "fastdeploy"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["paddle", "paddlenlp", "fastdeploy"])