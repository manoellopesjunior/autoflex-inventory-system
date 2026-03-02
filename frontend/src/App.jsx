import { useEffect, useState } from "react";
import "./App.css";

function App() {
  // Estados para produtos, matérias-primas e formulários
  const [products, setProducts] = useState([]);
  const [rawMaterials, setRawMaterials] = useState([]);
  const [productName, setProductName] = useState("");
  const [productPrice, setProductPrice] = useState("");
  const [rawName, setRawName] = useState("");
  const [rawStock, setRawStock] = useState("");
  const [selectedProduct, setSelectedProduct] = useState("");
  const [selectedRaw, setSelectedRaw] = useState("");
  const [quantity, setQuantity] = useState("");

  const baseUrl = "http://127.0.0.1:8000"; // URL do backend

  // Funções para buscar produtos e matérias-primas
  const fetchProducts = () => {
    fetch(`${baseUrl}/products/`)
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Erro ao buscar produtos:", err));
  };

  const fetchRawMaterials = () => {
    fetch(`${baseUrl}/raw-materials/`)
      .then((res) => res.json())
      .then((data) => setRawMaterials(data))
      .catch((err) => console.error("Erro ao buscar matérias-primas:", err));
  };

  useEffect(() => {
    fetchProducts();
    fetchRawMaterials();
  }, []);

  // Função para criar produto
  const handleCreateProduct = () => {
    if (!productName || !productPrice) return;
    fetch(`${baseUrl}/products/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: productName,
        price: parseFloat(productPrice),
      }),
    })
      .then(() => {
        setProductName("");
        setProductPrice("");
        fetchProducts();
      })
      .catch((err) => console.error("Erro ao criar produto:", err));
  };

  // Função para criar matéria-prima
  const handleCreateRaw = () => {
    if (!rawName || !rawStock) return;
    fetch(`${baseUrl}/raw-materials/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: rawName,
        stock: parseFloat(rawStock),
      }),
    })
      .then(() => {
        setRawName("");
        setRawStock("");
        fetchRawMaterials();
      })
      .catch((err) => console.error("Erro ao criar matéria-prima:", err));
  };

  // Função para deletar produto
  const handleDeleteProduct = (id) => {
    fetch(`${baseUrl}/products/${id}`, { method: "DELETE" })
      .then(() => fetchProducts())
      .catch((err) => console.error("Erro ao deletar produto:", err));
  };

  // Função para deletar matéria-prima
  const handleDeleteRaw = (id) => {
    fetch(`${baseUrl}/raw-materials/${id}`, { method: "DELETE" })
      .then(() => fetchRawMaterials())
      .catch((err) => console.error("Erro ao deletar matéria-prima:", err));
  };

  // Função para associar matéria-prima a produto
  const handleAddRawToProduct = () => {
    if (!selectedProduct || !selectedRaw || !quantity) return;
    fetch(`${baseUrl}/product-raw-materials/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        product_id: parseInt(selectedProduct),
        raw_material_id: parseInt(selectedRaw),
        quantity: parseFloat(quantity),
      }),
    })
      .then(() => {
        setSelectedProduct("");
        setSelectedRaw("");
        setQuantity("");
        fetchProducts(); // Atualiza a lista para refletir a associação
      })
      .catch((err) => console.error("Erro ao associar matéria-prima:", err));
  };

  return (
    <div className="container">
      <h1>Autoflex Inventory System</h1>

      {/* Formulários para cadastro */}
      <div className="forms">
        <div className="form-card">
          <h3>Criar Produto</h3>
          <input
            type="text"
            placeholder="Nome do produto"
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
          />
          <input
            type="number"
            placeholder="Preço"
            value={productPrice}
            onChange={(e) => setProductPrice(e.target.value)}
          />
          <button onClick={handleCreateProduct}>Adicionar Produto</button>
        </div>

        <div className="form-card">
          <h3>Criar Matéria-prima</h3>
          <input
            type="text"
            placeholder="Nome da matéria-prima"
            value={rawName}
            onChange={(e) => setRawName(e.target.value)}
          />
          <input
            type="number"
            placeholder="Estoque"
            value={rawStock}
            onChange={(e) => setRawStock(e.target.value)}
          />
          <button onClick={handleCreateRaw}>Adicionar Matéria-prima</button>
        </div>

        <div className="form-card">
          <h3>Associar Matéria-prima ao Produto</h3>
          <select
            value={selectedProduct}
            onChange={(e) => setSelectedProduct(e.target.value)}
          >
            <option value="">Selecione o produto</option>
            {products.map((p) => (
              <option key={p.id} value={p.id}>
                {p.name}
              </option>
            ))}
          </select>
          <select
            value={selectedRaw}
            onChange={(e) => setSelectedRaw(e.target.value)}
          >
            <option value="">Selecione a matéria-prima</option>
            {rawMaterials.map((r) => (
              <option key={r.id} value={r.id}>
                {r.name}
              </option>
            ))}
          </select>
          <input
            type="number"
            placeholder="Quantidade"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
          />
          <button onClick={handleAddRawToProduct}>Adicionar Associação</button>
        </div>
      </div>

      {/* Listagem de Produtos */}
      <div className="lists">
        <div className="list-card">
          <h2>Produtos</h2>
          {products.length === 0 ? (
            <p>Nenhum produto encontrado.</p>
          ) : (
            <table>
              <thead>
                <tr>
                  <th>Nome</th>
                  <th>Preço</th>
                  <th>Matérias-primas</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {products.map((p) => (
                  <tr key={p.id}>
                    <td>{p.name}</td>
                    <td>R$ {p.price.toFixed(2)}</td>
                    <td>
                      {p.raw_materials && p.raw_materials.length > 0 ? (
                        <ul>
                          {p.raw_materials.map((rm) => (
                            <li key={`${p.id}-${rm.raw_material_id}`}>
                              {rawMaterials.find(
                                (raw) => raw.id === rm.raw_material_id
                              )?.name || "?"} - Qty: {rm.quantity}
                            </li>
                          ))}
                        </ul>
                      ) : (
                        <span>—</span>
                      )}
                    </td>
                    <td>
                      <button
                        className="delete-btn"
                        onClick={() => handleDeleteProduct(p.id)}
                      >
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>

        {/* Listagem de Matérias-primas */}
        <div className="list-card">
          <h2>Matérias-primas</h2>
          {rawMaterials.length === 0 ? (
            <p>Nenhuma matéria-prima encontrada.</p>
          ) : (
            <table>
              <thead>
                <tr>
                  <th>Nome</th>
                  <th>Estoque</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {rawMaterials.map((r) => (
                  <tr key={r.id}>
                    <td>{r.name}</td>
                    <td>{r.stock}</td>
                    <td>
                      <button
                        className="delete-btn"
                        onClick={() => handleDeleteRaw(r.id)}
                      >
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;