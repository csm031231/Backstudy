import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

const API_URL = 'http://3.36.76.75:8000'; // API URL 수정

export default function Login() {
  const [email, setEmail] = useState(""); // 유저이름을 email로 변경
  const [pw, setPw] = useState(""); // 비밀번호 상태 변수 추가
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      // 로그인 API 요청 수정
      const response = await axios.post(
        `${API_URL}/user/Login`, 
        `username=${email}&password=${pw}`,
        {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        }
      );
      const newToken = response.data.access_token;
      localStorage.setItem("access_token", newToken); // 토큰 로컬스토리지에 저장
      console.log("로그인 성공:", response.data);
      navigate("/mypage");  // 로그인 후 마이페이지로 리디렉션
    } catch (error) {
      console.error("로그인 실패:", error);
    }
  };

  return (
    <div className="container">
      <h2>로그인</h2>
      <form onSubmit={handleLogin}>
        <input 
          type="text" 
          placeholder="유저이름" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <input 
          type="password" 
          placeholder="비밀번호" 
          value={pw} 
          onChange={(e) => setPw(e.target.value)} 
        />
        <button type="submit">로그인</button>
      </form>
    </div>
  );
}
