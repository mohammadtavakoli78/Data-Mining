import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def load_data_set():
    df = pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
    return df


def count_nan_value(data_set):
    return [data_set['sepal_length'].sum(), data_set['sepal_width'].sum(), data_set['petal_length'].sum(),
            data_set['petal_width'].sum(), data_set['target'].sum()]


def dropna(data_set):
    return data_set.dropna()


def label_encoder(data_set):
    le = preprocessing.LabelEncoder()
    data_set['target'] = le.fit_transform(data_set['target'])
    return data_set


def normalization(data_set):
    scaler = StandardScaler()
    new_data_set = scaler.fit_transform(data_set.iloc[:, 0:-1])
    df_numpy = np.append(new_data_set, data_set[['target']].to_numpy(), axis=1)
    data_set = pd.DataFrame(df_numpy, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
    return data_set


def show_var(data_set):
    variances = data_set.iloc[:, 0:-1].var()
    print(data_set.iloc[:, 0:-1].describe())
    print('var', end="        ")
    for i in variances.values:
        print(format(i, ".6f"), end="     ")
    print('\n')


def pca(data_set):
    target = data_set[['target']]
    data_set = data_set.iloc[:, 0:-1]
    pca = PCA(n_components=2)
    data_set = pca.fit_transform(data_set)
    new_data_set = pd.DataFrame(data=data_set, columns=['feature 1', 'feature 2'])
    new_data_set = pd.concat([new_data_set, target], axis=1)
    new_data_set = dropna(new_data_set)
    return data_set, new_data_set


def draw(data_set):
    colors = {'0': 'r', '1': 'g', '2': 'b'}
    # create a figure and axis
    fig, ax = plt.subplots()
    # plot each data-point
    for i in range(len(data_set['feature 1'])):
        if i in list(data_set['target']._index):
            ax.scatter(data_set['feature 1'][i], data_set['feature 2'][i], color=colors[str(int(data_set['target'][i]))])
    # set a title and labels
    ax.set_title('Iris Dataset')
    ax.set_xlabel('feature 1')
    ax.set_ylabel('feature 2')

    ax.legend()
    plt.show()


if __name__ == "__main__":
    df = load_data_set()

    print(count_nan_value(df.isna()))
    df = dropna(df)

    df = label_encoder(df)
    # print(df)

    show_var(df)
    df = normalization(df)
    show_var(df)

    new_data_set = pd.DataFrame(df, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
    boxplot = new_data_set.boxplot(column=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

    df = pca(df)
    # print(df[1])

    draw(df[1])
