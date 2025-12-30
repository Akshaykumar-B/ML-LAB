import pandas as pd

data = pd.read_csv("candidate.csv")

attributes = data.columns[:-1]
S = ['Ø'] * len(attributes)
G = [['?'] * len(attributes)]

for _, row in data.iterrows():
    if row.iloc[-1] == 'Yes':
        for i in range(len(attributes)):
            if S[i] == 'Ø':
                S[i] = row.iloc[i]
            elif S[i] != row.iloc[i]:
                S[i] = '?'
        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(len(S)))]
    else:
        new_G = []
        for g in G:
            for i in range(len(attributes)):
                if g[i] == '?' and S[i] != row.iloc[i]:
                    h = g.copy()
                    h[i] = S[i]
                    new_G.append(h)
        G = new_G

print("Specific Hypothesis:", S)
print("General Hypotheses:", G)
