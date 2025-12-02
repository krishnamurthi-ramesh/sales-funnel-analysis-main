import subprocess
import os
import sys


def test_run_analysis_creates_chart():
    python_exe = sys.executable
    result = subprocess.run([python_exe, 'run_analysis.py'], capture_output=True)
    assert result.returncode == 0, f"Script failed with return code {result.returncode}, stderr: {result.stderr}"
    assert os.path.exists('sales_funnel_chart.png'), 'sales_funnel_chart.png was not created'
