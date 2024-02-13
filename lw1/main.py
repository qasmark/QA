import subprocess


def run_tests(test_file, answer_file):
    with open(test_file, 'r') as f_tests, open(answer_file, 'r') as f_answers:
        tests = f_tests.readlines()
        answers = f_answers.readlines()

        if len(tests) != len(answers):
            print("Error! The number of tests does not match the number of answers.")
            return

        for i, test in enumerate(tests):
            test = test.strip()
            answer = answers[i].strip()

            try:
                output = subprocess.check_output(['python', 'triangle_checking.py'] + test.split(), input=test,
                                                 universal_newlines=True,
                                                 timeout=5)
                output = output.strip()

                if output != answer:
                    print(f"Error at the test {i + 1}:\nExcpected output: {answer}\nResponse output: {output}")
                else:
                    print(f"Test {i + 1} success!")

            except subprocess.TimeoutExpired:
                print(f"Test {i + 1}: runtime error")

            except Exception as e:
                print(f"Error at the test {i + 1}: {str(e)}")


run_tests("test_cases.txt", "answers.txt")