from matplotlib import pyplot as plt
from os import listdir
import pandas as pd
import numpy as np
from pandas._config.config import options

pd.set_option("display.max_columns", None)

print(*[file_name.split(".")[0] for file_name in listdir("opinions")], sep="\n")
product_id = input("Podaj kod produktu: ")

opinions = pd.read_json("opinions/{}.json".format(product_id))

opinions.stars = opinions.stars.map(
    lambda stars: float(stars.split("/")[0].replace(",", ".")))

opinions_count = opinions.opinion_id.count()
# opinions_count = len(opinions.index)
# opinions_count = opinions.shape[0]
pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()
average_score = opinions.stars.mean().round(2)

stars = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value=0)

stars.plot.bar(color="cornflowerblue")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
#plt.show()
plt.savefig(f"plots{product_id}bar.png")
plt.close()

recomm = opinions.recomm.value_counts(dropna=False).sort_index()
names = 'Polecam', 'Nie Polecam', 'Nie mam zdania'
recomm.plot.pie(
    shadow= True , 
    autopct='%1.1f%%', 
    colors=['crimson', 'forestgreen', 'gold'],
    labels = names,
    startangle = 30,
    )
plt.title("Rekomendacje")
plt.ylabel(" ")
plt.savefig(f"plots{product_id}pie.png")
#plt.show()