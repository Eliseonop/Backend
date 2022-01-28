import { hashSync } from "bcrypt";
export default async (prisma) => {
  const password = hashSync("Welcome123!", 10);
  //corremos el comando > npx prisma db seed
  await prisma.usuario.upsert({
    create: {
      nombre: "eliseo",
      correo: "eliseonop@gmail.com",
      password,
      tipoUsuario: "ADMIN",
    },
    update: {
      password,
    },
    where: {
      //solamente se declara las columnas que sean unicas (unique) o las pk
      correo: "eliseonop@gmail.com",
    },
  });
};
