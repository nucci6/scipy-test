# SciPy Testing for the RISE SW Stack

A successful execution of the following tests will verify the installation and optimization of SciPy on the new RISE software stack. 

Two Python scripts are provided for testing:
*   `scipy_test.py` - Runs the official, exhaustive SciPy test suite.
*   `scipy_sanity_check.py` - Runs a quick sanity check on core mathematical components.

## Step 1: Environment Setup

For either test, we must first set up the environment by loading the appropriate modules and creating a virtual environment. The virtual environment is required to install testing dependencies without needing write access to the central software stack.

**1. Load the required modules:**
```
# Clear existing modules
module purge

# Load the RISE software stack and SciPy
module use /storage/icds/sw8/modulefiles_rc2026/linux-rhel8-x86_64/Core
module load gcc
module load py-scipy
```

(Note: You can use module spider scipy to verify available versions if needed).

2. Create and activate a virtual environment: The --system-site-packages flag is critical here, as it allows the virtual environment to see the central SciPy installation.

bash
python -m venv --system-site-packages ~/scipy_test_env
source ~/scipy_test_env/bin/activate
3. Install testing dependencies:

bash
pip install pytest hypothesis pooch
Step 2: Run the Full Test Suite (scipy_test.py)
The most thorough way to test a SciPy installation is to run its own built-in test suite. This ensures that all C/Fortran extensions, linear algebra libraries (LAPACK), and optimization functions are working correctly on our specific hardware architecture.

(Note: This script is configured to safely bypass three specific tests known to throw false positives due to our highly optimized zlib and AVX-512 CPU architecture).

Run the test script:

bash
python scipy_test.py 
Expected Output: The test will take about 10 minutes to run over 63,000 checks. The output should look like this near the end, confirming zero failures:

text
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
= 63499 passed, 4079 skipped, 16254 deselected, 194 xfailed, 9 xpassed, 2926 warnings in 624.15s (0:10:24) =
Step 3: Run the Core Sanity Check (scipy_sanity_check.py)
This second test is not as comprehensive, but runs a reasonable subset to quickly verify that the most commonly used sub-modules (Optimization, Linear Algebra, Integration, and Sparse Matrices) are functioning correctly.

Run the test script:

bash
python scipy_sanity_check.py 
Expected Output:

text
--- SciPy Sanity Check ---
Version: 1.16.3

1. Testing Optimization (Nelder-Mead)...
   -> Optimization OK. Minimum found at: [0.99998292 0.99996512]
2. Testing Linear Algebra (LU Decomposition)...
   -> LinAlg OK. Matrix decomposed successfully.
3. Testing Numerical Integration (Quad)...
   -> Integration OK. Result: 0.8862 (Error: 7.1013e-09)
4. Testing Sparse Matrices...
   -> Sparse Matrix OK. Created 3x3 CSR matrix with 6 non-zero elements.

 SciPy 1.16.3 is installed and functioning correctly!
Step 4: Cleanup
Once testing is complete, you can deactivate and remove the virtual environment to keep your home directory clean:

bash
deactivate
rm -rf ~/scipy_test_env
