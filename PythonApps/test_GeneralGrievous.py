from testplan import test_plan
from testplan.testing.multitest import MultiTest, testsuite, testcase
from GeneralGrievous import answerToKenobi

@testsuite
class GeneralGrievousTests:

    @testcase
    def test_answer_to_kenobi(self, env, result):
        result.equal(answerToKenobi('Hello there!'), "General Kenobi!")
        result.equal(answerToKenobi('You underestimate my power!'), "General Skywalker, I expected someone taller.")
        
@test_plan(name="General Grievous Test Plan")
def main(plan):
    plan.add(MultiTest(name="General Grievous Tests", suites=[GeneralGrievousTests()]))

if __name__ == "__main__":
    main()