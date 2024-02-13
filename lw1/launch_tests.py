import subprocess


def run_tests(test_file):
    with open(test_file, 'r') as f_tests:
        tests = f_tests.readlines()

        for i, test in enumerate(tests):
            test = test.strip()

            try:
                output = subprocess.check_output(['python', 'triangle_checking.py'] + test.split(), input=test,
                                                 universal_newlines=True,
                                                 timeout=5)
                output = output.strip()
                print(f"Test {i + 1} shows the result:")

            except subprocess.TimeoutExpired:
                print(f"Test {i + 1}: runtime error")

            except Exception as e:
                print(f"Error at the test {i + 1}: {str(e)}")


run_tests("test_cases.txt")