import "./App.css";
import { Navigation } from "./components/Navigation";
import { Auth } from "./pages/Auth";
import { Home } from "./pages/Home";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { CreateEditBlogPost } from "./pages/CreateEditBlogPost";
import { AuthProvider } from "./context/AuthProvider";

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <Router>
          <Navigation />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/auth" element={<Auth />} />
            <Route path="/new" element={<CreateEditBlogPost />} />
          </Routes>
        </Router>
      </AuthProvider>
    </div>
  );
}

export default App;