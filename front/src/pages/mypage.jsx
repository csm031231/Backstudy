import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

const API_URL = 'http://3.39.233.182:8000';  // API URL 수정

export default function MyPage() {
  const [username, setUsername] = useState("사용자");
  const [email, setEmail] = useState("user@example.com");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleUpdate = async () => {
    try {
      const updatedData = { username, password, email };
      const response = await axios.put(
        `${API_URL}/user/${username}/change`,  // API 경로 수정
        updatedData
      );
      console.log("정보 수정 성공:", response.data);
      navigate("/mypage");  // 수정 후 마이페이지로 리디렉션
    } catch (error) {
      console.error("정보 수정 실패:", error);
    }
  };

  return (
    <div className="container">
      <h2>정보 수정</h2>
      <form onSubmit={(e) => e.preventDefault()}>
        <input 
          type="text" 
          value={username} 
          onChange={(e) => setUsername(e.target.value)} 
        />
        <input 
          type="email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <input 
          type="password" 
          placeholder="새 비밀번호" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        />
        <button type="submit" onClick={handleUpdate}>정보 수정</button>
      </form>
    </div>
  );
}
