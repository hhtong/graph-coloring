# Copyright 2020 D-Wave Systems Inc.
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

import subprocess
import unittest
import time
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class IntegrationTests(unittest.TestCase):
    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_graph_coloring(self):
        file_path = os.path.join(project_dir, 'graph_coloring.py')
        output = subprocess.check_output([sys.executable, file_path])
        output = str(output).upper()
        if os.getenv('DEBUG_OUTPUT'):
            print("Example output \n" + output)

        with self.subTest(msg="Verify if solution validity:  True \n"):
            self.assertIn("Solution validity:  True".upper(), output)

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_map_coloring(self):
        """Run map_coloring.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'map_coloring.py')
        subprocess.check_output([sys.executable, demo_file])

if __name__ == '__main__':
    unittest.main()
