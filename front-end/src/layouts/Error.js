import styled from "styled-components";

export default function ErrorLayout({ children }) {
  return (
    <Container>
      {children}
    </Container>
  );
}

const Container = styled.div`
  min-height: 100vh;
  width: 100%;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: #1A1A1A;
  color: #FAFAFA;
`;
