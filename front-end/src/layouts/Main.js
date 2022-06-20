import styled from "styled-components";

export default function MainLayout({ children }) {
  return (
    <Container>
      {children}
    </Container>
  );
}

const Container = styled.div`
  min-height: 100vh;
  width: 100%;
  max-width: 1180px;
  display: flex;
  margin: 0 auto;
  gap: 28px;

  & > aside {
    padding: 18px 15px;
  }

  & > aside:nth-of-type(1) {
    padding-left: 0;
    width: 256px;
  }

  & > main {
    flex-shrink: 0;
    width: min(560px, 100%);
    border-left: 1px solid #EFF3F4;
    border-right: 1px solid #EFF3F4;
    padding: 18px 15px;
  }

  & > aside:nth-of-type(3) {
    padding-right: 0;
    width: 364px;
  }
`;
