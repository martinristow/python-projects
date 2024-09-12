# vcituvanje go padnas modulot
import pandas as pd
# preku pandas modolut go citame csv fajlot
df = pd.read_csv('salaries_by_college_major.csv')

# --------------------------------------------------------------

# so metodot head() gi dobivame prvite 5 redici od DataFrame
df.head()

# --------------------------------------------------------------

# so shape kje videme kolku redici i koloni imame vo nasiot csv fajl
print(df.shape)

# --------------------------------------------------------------

# so columns ke gi dobieme iminjata na site koloni koj sto gi imame vo nasiot DataFrame
print(df.columns)

# --------------------------------------------------------------

# isna() metodot proveruva dali objektite od df(Dataframe) ili serija sodrzat vrednosti
# sto nedostasuvaat ili nula(NA, NaN) i vrakja nov objekt so ista forma kako originalot, no
# so bulovi vrednosti True ili false kako elementi. True oznacuva prisustvo na nula ili
# isceznati vrednosti, a False oznacuva poinaku
print(df.isna)

# --------------------------------------------------------------

# tail() metodot ni gi vrakja poslednite nekolku redovi od Dataframot
print(df.tail())

# --------------------------------------------------------------

# dropna() metodot gi otstranuva redovite sto sodrzat NULL vrednosti. Metodot dropna
# vrakja nov objekt DataFrame, osven ako parametarot na mesto e postaven na True, vo toj
# slucaj metodot dropna() go otstranuva otstranuvanjeto vo originalnata DataFrame.
clean_df = df.dropna()
print(clean_df.isna)
print(clean_df.tail())

# --------------------------------------------------------------

# What college major has the highest mid-career salary? How much do graduates with this major earn?
# (Mid-career is defined as having 10+ years of experience).
clean_df['Mid-Career Median Salary'].idxmax()
print(clean_df['Mid-Career Median Salary'].loc[8])
print(clean_df['Undergraduate Major'][8])

# print(clean_df['Mid-Career Median Salary'].max())
# print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
# clean_df['Undergraduate Major'][8]

# --------------------------------------------------------------

# Which college major has the lowest starting salary and how much do graduates earn after university?
# The Lowest Starting and Mid-Career Salary
clean_df['Starting Median Salary'].idxmin()
print(clean_df['Starting Median Salary'][49])
print(clean_df['Undergraduate Major'][49])


# The Lowest Starting and Mid-Career Salary
# print(clean_df['Starting Median Salary'].min())
# clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

# --------------------------------------------------------------

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
clean_df['Mid-Career Median Salary'].idxmin()
print(clean_df['Mid-Career Median Salary'][18])
print(clean_df['Undergraduate Major'][18])

# clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]
