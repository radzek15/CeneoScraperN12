from os import listdir
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)


print(*[file_name.split(".")[0] for file_name in listdir("opinions")], sep="\n")

product_id = input("Podaj kod produktu: ")
opinions = pd.read_json('opinions/{}.json'.format(product_id))

opinions.stars =  opinions.stars.apply(
    lambda stars : float(stars.split('/')[0].replace(',', '.')))

opinions_count = opinions.opinion_id.count()
#opinions_count = opinions.shape[0]
#opinions_count = print(len(opinions.index))
pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()
average_score = opinions.stars.mean().round(2)

stars = opinions.stars.value_counts().reindex(np.arange(0, 5.5, .5), fill_value=0)
stars.plot.bar()
plt.title('Gwiazdki')
plt.xlabel('Liczba gwiazdek')
plt.ylabel('Liczba opinii')
#plt.savefig('plots/{}.png'.format(product_id))
plt.close()

recomm = opinions.recomm.value_counts(dropna=False).sort_index()

recomm.plot.pie()
plt.show()
