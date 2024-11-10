# Titre de l'application
st.title("Concours de Répétitions de Pompes")

# Saisie du nombre de répétitions
reps = st.number_input("Entrez votre nombre de répétitions :", min_value=1, step=1)

# Enregistrer les répétitions
if "reps_data" not in st.session_state:
    st.session_state.reps_data = []

if st.button("Soumettre"):
    st.session_state.reps_data.append(reps)
    st.success("Nombre de répétitions ajouté !")

# Calculer la distribution des répétitions
if st.session_state.reps_data:
    df = pd.DataFrame(st.session_state.reps_data, columns=["reps"])
    rep_counts = df["reps"].value_counts().sort_index()

    # Affichage du graphique
    st.subheader("Distribution des Répétitions")
    plt.figure(figsize=(10, 6))
    plt.bar(rep_counts.index, rep_counts.values)
    plt.xlabel("Nombre de Répétitions")
    plt.ylabel("Nombre de Participants")
    plt.title("Nombre de Personnes par Nombre de Répétitions")
    st.pyplot(plt.gcf())
