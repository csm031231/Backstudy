import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import MyPage from "./pages/mypage";
import Home from "./pages/Home";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/mypage" element={<MyPage />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}
