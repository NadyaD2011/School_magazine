import pandas as pd
from random import randint


def class_jurnal(klass_jurnal, col_good_students, column):
    top = (
        klass_jurnal.sort_values(by="mean", ascending=False)
        .head(col_good_students)
        .reset_index(drop=True)
    )
    result = klass_jurnal.pivot_table(
        index=column,
        columns="matem",
        values="mean",
        aggfunc="count",
        fill_value=0,
    )

    return result, top


def create_klass_jurnal(klass):
    table = pd.DataFrame(klass)
    table = table.melt()
    table = table.rename(columns={"variable": "bukva", "value": "name"})

    subjects = ["matem", "rus", "inform"]
    for i in range(len(subjects)):
        subjects_evaluations = [randint(3, 5) for i in range(len(table))]
        table[subjects[i]] = subjects_evaluations

    table["mean"] = (table["matem"] + table["rus"] + table["inform"]) / 3
    spis = [9 if i % 2 == 1 else 10 for i in range(len(table))]
    table["parall"] = spis
    table = table[["parall", "bukva", "name", "matem", "rus", "inform", "mean"]]

    return table


def analysis_performance(klass_jurnal):
    result_analysis = klass_jurnal.pivot_table(
        index="bukva",
        columns="parall",
        values="mean",
        aggfunc="mean",
        fill_value=0,
    )
    return result_analysis


def main():
    klass = {
        "A": [
            "Сидоров",
            "Мишкин",
            "Копытов",
            "Мишеллиа",
            "Попов",
            "Инкогнитов",
            "Белов",
            "Чернов",
            "Михайлов",
            "Полинова",
        ],
        "B": [
            "Синяков",
            "Синев",
            "Желтухин",
            "Горшков",
            "Желтов",
            "Виноградова",
            "Иванов",
            "Мирзин",
            "Петин",
            "Машинон",
        ],
    }
    klass_jurnal = create_klass_jurnal(klass)
    result, top = class_jurnal(klass_jurnal, 5, "bukva")
    result_analysis = analysis_performance(klass_jurnal)


if __name__ == "__main__":
    main()
