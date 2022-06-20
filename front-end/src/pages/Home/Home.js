import MainLayout from "../../layouts/Main";

import Menu from "./Menu";

export default function Home() {
  return (
    <MainLayout>
      <aside>
        <Menu />  
      </aside>  
      <main>Main</main>
      <aside>Lateral</aside>
    </MainLayout>
  );
}
