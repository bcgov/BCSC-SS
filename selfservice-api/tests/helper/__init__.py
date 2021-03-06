# Copyright © 2019 Province of British Columbia
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
"""Helper functions for testing."""

import re


def camel2snake(camel_dict: dict):
    """Convert the passed dictionary's keys from camelCase to snake_case."""
    converted_obj = {}
    for key in camel_dict.keys():
        converted_key = re.sub(r'[A-Z]', lambda x: '_' + x.group(0).lower(), key)
        if type(camel_dict[key]) is dict:
            converted_obj[converted_key] = camel2snake(camel_dict[key])
        elif type(camel_dict[key]) is list:
            converted_list = []
            for list_value in camel_dict[key]:
                if type(list_value) is dict:
                    converted_list.append(camel2snake(list_value))
                else:
                    break
            if len(converted_list) > 0:
                converted_obj[converted_key] = converted_list
            else:
                converted_obj[converted_key] = camel_dict[key]
        else:
            converted_obj[converted_key] = camel_dict[key]
    return converted_obj
