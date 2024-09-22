import pandas as pd
from random import randint

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


table_sort = table.sort_values(by="mean", ascending=False).head(10)
table_sort = table_sort.reset_index(drop=True)

klass_table = table.groupby(by="bukva").mean(numeric_only=True)
klass_table = table.pivot_table(
    index="parall", columns="bukva", values="mean", aggfunc="mean"
)
klass_table = table.pivot_table(
    index=["parall", "bukva"],
    columns="matem",
    values="mean",
    aggfunc="count",
    fill_value=0,
)

print(klass_table)
