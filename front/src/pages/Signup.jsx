import { useState } from "react";
import axios from 'axios';

const API_URL = 'http://3.39.233.182:8000';  // API URL 수정

export default function Signup() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${API_URL}/user/`,  // API 경로 수정
        { username, password, email }
      );
      console.log("회원가입 성공:", response.data);
    } catch (error) {
      console.error("회원가입 실패:", error);
    }
  };

  return (
    <div className="container">
      <h2>회원가입</h2>
      <form onSubmit={handleSignup}>
        <input 
          type="text" 
          placeholder="유저이름" 
          value={username} 
          onChange={(e) => setUsername(e.target.value)} 
        />
        <input 
          type="email" 
          placeholder="이메일" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <input 
          type="password" 
          placeholder="비밀번호" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        />
        <button type="submit">회원가입</button>
      </form>
    </div>
  );
}
