import mongoose from "mongoose";
import express, { json } from "express";

const app = express();
app.use(json());
const PORT = process.env.PORT ?? 3000;

app.listen(PORT, async function () {
  try {
    console.log(`Servidor corriendo en el puerto local ${PORT}`);
    await mongoose.connect("mongodb://localhost:27017");
    console.log("se conecto a la base de datos");
    // console.log(respuesta);
  } catch (error) {
    console.log(error);
  }
});
