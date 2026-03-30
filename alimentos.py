from alimentos import inserir_alimento, conectar


def limpar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alimentos")
    conn.commit()
    conn.close()


def test_integracao_simples():

    limpar()

    inserir_alimento("A", "C", "BR")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT cod, sec FROM alimentos")
    resultado = cursor.fetchone()

    assert resultado[0] == "BRA0001C"
    assert resultado[1] == 1

    conn.close()


def test_incremento():

    limpar()

    inserir_alimento("A", "C", "BR")
    inserir_alimento("A", "B", "BR")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT cod FROM alimentos ORDER BY id")
    resultados = cursor.fetchall()

    assert resultados[0][0] == "BRA0001C"
    assert resultados[1][0] == "BRA0002B"

    conn.close()
