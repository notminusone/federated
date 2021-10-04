# Copyright 2021, Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Base configuration."""

from ml_collections.config_dict import config_dict


def get_config():
  """Returns config dictionary for model."""
  config = dict(
      name="defaults",
      # Either use unbiased data, biased data, or same data i.e., data variable
      # can take one of "biased_data", "unbiased_data", "same_data".
      data="biased_data",
      # Flags to indicate which methods to compare.
      run_approx_miracle=True,
      run_miracle=False,
      run_modified_miracle=True,
      run_privunit=True,
      run_sqkr=True,
      # Common parameters.
      num_itr=5,
      coding_cost=4,
      coding_cost_multiplier=1,
      # Specific parameters (leave them as they are for now).
      delta=10**(-6),
      budget=0.5,
      alpha=1.0,
      # Variation.
      vary="eps",  # Can take one of "d", "n", "eps".
      d_space=[50, 100],
      n_space=[2500, 5000, 7500, 10000],
      eps_space=[1],
      # Defaults.
      n=1000,
      d=500,
      t=6,
      epsilon_target=2,
  )
  config = config_dict.ConfigDict(config)
  config.lock()  # Prevent addition of new fields.
  return config
