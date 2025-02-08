import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="container">
      <h2>홈</h2>
      <Link to="/signup">회원가입</Link>
      <Link to="/login">로그인</Link>
      <Link to="/mypage">마이페이지</Link>
    </div>
  );
}
