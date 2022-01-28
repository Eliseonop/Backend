import express, { json } from "express";
import morgan from "morgan";
import { authRouter } from "./routes/auth.routes.js";

const app = express();
const PORT = process.env.PORT ?? 3000;

app.use(morgan("dev"));
app.use(json());

//defino mis rutas
app.use(authRouter);

app.listen(PORT, () => {
  console.log(`servidor corriendo en el puerto ${PORT}`);
});

// vamos a usar morgan
