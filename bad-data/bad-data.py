import datasets

class BadData(datasets.GeneratorBasedBuilder):
    def _info(self):
        features = datasets.Features(
            {
                "value": datasets.Value("float"),
            }
        )
        return datasets.DatasetInfo(features=features)

    def _split_generators(self, dl_manager):
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={})
        ]


    def _generate_examples(self):
        yield (0, {"value": None})
