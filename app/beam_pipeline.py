import apache_beam as beam
import pandas as pd


class TransformSchema(beam.DoFn):

    def process(self, element):
        yield element


def run_pipeline():

    data = pd.read_csv(
        "data/oracle_schema.csv"
    )

    records = data.to_dict(
        orient="records"
    )

    with beam.Pipeline() as p:

        (
            p
            | "Create" >> beam.Create(records)
            | "Transform" >> beam.ParDo(
                TransformSchema()
            )
            | "Print" >> beam.Map(print)
        )


if __name__ == "__main__":
    run_pipeline()