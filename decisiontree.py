import pandas as pd
import numpy as np
import pickle
import streamlit as st

def main():
    dataset = pd.read_csv("bill_authentication.csv")
    dataset = dataset.drop_duplicates()
    x = dataset.iloc[:, 0:4]
    y = dataset.iloc[:, 4]

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.fit_transform(x_test)

    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=20, random_state=0)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    # print(classifier.predict(np.array([0.3,0.3,0.2,0.1]).reshape(1,-1))
    # )

    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    # print(confusion_matrix(y_test,y_pred))
    # print(classification_report(y_test,y_pred))
    # print(accuracy_score(y_test,y_pred))
    #
    with open("model.pkl", "wb") as f:
        pickle.dump(classifier, f)
    with open("model.pkl", "rb") as f:
        mp = pickle.load(f)
    # print(mp.predict(np.array([0.3,0.3,0.2,0.1]).reshape(1,-1)))

    st.title("Decision Tree Classifier")

    # input

    variance = (st.text_input("Enter the variance you would like to use:"))
    Skewness = (st.text_input("Enter the skewness you would like to use:"))
    Curtosis = (st.text_input("Enter the curtosis you would like to use:"))
    Entropy = (st.text_input("Enter the entropy you would like to use:"))
    if st.button("Predict"):
        makeprediction = mp.predict(np.array([variance, Skewness, Curtosis, Entropy]).reshape(1, -1))
        output = round(makeprediction[0], 2)
        st.success(f"CLASS IS {output}")
if __name__ == "__main__":
 main()
 
# import pandas as pd
# import numpy as np
# import pickle
# import streamlit as st

# def main():
#     # Load and clean dataset
#     dataset = pd.read_csv("bill_authentication.csv")
#     dataset = dataset.drop_duplicates()
#     x = dataset.iloc[:, 0:4]
#     y = dataset.iloc[:, 4]

#     # Train/test split
#     from sklearn.model_selection import train_test_split
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#     # Standardize
#     from sklearn.preprocessing import StandardScaler
#     sc = StandardScaler()
#     x_train = sc.fit_transform(x_train)
#     x_test = sc.transform(x_test)

#     # Train classifier
#     from sklearn.ensemble import RandomForestClassifier
#     classifier = RandomForestClassifier(n_estimators=20, random_state=0)
#     classifier.fit(x_train, y_train)

#     # Save model
#     with open("model.pkl", "wb") as f:
#         pickle.dump(classifier, f)

#     # Load model
#     with open("model.pkl", "rb") as f:
#         model = pickle.load(f)

#     # Streamlit UI
#     st.title("Random Forest Classifier for Banknote Authentication")

#     # Inputs
#     try:
#         variance = float(st.text_input("Enter the Variance:"))
#         skewness = float(st.text_input("Enter the Skewness:"))
#         curtosis = float(st.text_input("Enter the Curtosis:"))
#         entropy = float(st.text_input("Enter the Entropy:"))

#         if st.button("Predict"):
#             input_data = np.array([variance, skewness, curtosis, entropy]).reshape(1, -1)
#             prediction = model.predict(input_data)
#             st.success(f"Predicted Class: {prediction[0]}")
#     except ValueError:
#         st.warning("Please enter valid numerical values for all inputs.")

# if __name__ == "__main__":
#     main()
