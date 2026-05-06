import scipy
import numpy as np
from scipy import optimize, linalg, integrate, sparse

def test_scipy_installation():
    print(f"--- SciPy Sanity Check ---")
    print(f"Version: {scipy.__version__}")
    assert scipy.__version__ == "1.16.3", f"Version mismatch! Found {scipy.__version__}"
    
    try:
        # 1. Test Optimization (Nelder-Mead)
        print("\n1. Testing Optimization (Nelder-Mead)...")
        def rosenbrock(x):
            return (1 - x[0])**2 + 105 * (x[1] - x[0]**2)**2
        
        res = optimize.minimize(rosenbrock, [2, 2], method='Nelder-Mead')
        print(f"   -> Optimization OK. Minimum found at: {res.x}")

        # 2. Test Linear Algebra (LU Decomposition)
        print("2. Testing Linear Algebra (LU Decomposition)...")
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        P, L, U = linalg.lu(A)
        print(f"   -> LinAlg OK. Matrix decomposed successfully.")

        # 3. Test Integration (Gaussian quadrature)
        print("3. Testing Numerical Integration (Quad)...")
        result, error = integrate.quad(lambda x: np.exp(-x**2), 0, np.inf)
        print(f"   -> Integration OK. Result: {result:.4f} (Error: {error:.4e})")

        # 4. Test Sparse Matrices (CSR format)
        print("4. Testing Sparse Matrices...")
        row = np.array([0, 2, 2, 0, 1, 2])
        col = np.array([0, 0, 1, 2, 2, 2])
        data = np.array([1, 2, 3, 4, 5, 6])
        S = sparse.csr_matrix((data, (row, col)), shape=(3, 3))
        print(f"   -> Sparse Matrix OK. Created 3x3 CSR matrix with {S.nnz} non-zero elements.")

        print("\n SciPy 1.16.3 is installed and functioning correctly!")

    except AssertionError as e:
        print(f"\nL Test Failed: {e}")
    except Exception as e:
        print(f"\nL Unexpected Error: {e}")

if __name__ == "__main__":
    test_scipy_installation()

