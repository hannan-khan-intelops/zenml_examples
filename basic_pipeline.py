from zenml.steps import step, Output
from zenml.pipelines import pipeline


@step
def step_one() -> Output(output_a=int, output_b=int):
    """This step returns the predefined values for a and b."""
    return 5, 12


@step
def step_two(input_a: int, input_b: int) -> Output(output_sum=int):
    """This step will add the inputs and return the sum as the output."""
    return input_a + input_b


@pipeline
def pipeline_one(step_1, step_2):
    output_a, output_b = step_1()
    output_sum = step_2(output_a, output_b)
    print(f"{output_sum = }")


if __name__ == "__main__":
    # execute one single step using entrypoint.
    print(step_one.entrypoint())
    print(step_two.entrypoint(*step_one.entrypoint()))

    # creating a pipeline object and running it in code.
    pipeline_one(step_1=step_one(), step_2=step_two()).run()
