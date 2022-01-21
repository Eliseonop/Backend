// const express = require("express");
import express, { json } from "express";
const app = express();
const PORT = 3000;

const productos = [
  {
    nombre: "arroz",
    precio: 25.9,
    estado: true,
  },
  {
    nombre: "Papel",
    precio: 2.9,
    estado: false,
  },
];

app.use(json());
app.get("/", (req, res) => {
  //req > es la informacion que me viene del cliente
  // rees > es la respuesta que le dare  al cliente
  res.status(200).json({
    message: "Peticion realizada existosamente",
  });
});

app.post("/producto", (req, res) => {
  console.log(req.body);
  if (req.body) {
    productos.push(req.body);
    return res.status(201).json({
      message: "producto agregado",
      producto: req.body,
    });
  } else {
    res.status(400).json({
      message: "informacion incorrecta",
    });
  }
});
app.get("/productos", (req, res) => {
  console.log(res);
  res.json({
    message: "informacion",
    content: productos,
  });
});
//route
app
  .route("/producto/:id")
  .get((req, res) => {
    //destructuring
    const { id } = req.params;
    // console.log(typeof +id);
    // const num = +id;

    if (productos[id - 1]) {
      return res.status(201).json({
        message: "producto encontrado",
        content: productos[id - 1],
      });
    } else {
      return res.status(400).json({
        message: "Producto no encontrado incorrecta",
        content: null,
      });
    }
  })
  .put((req, res) => {
    const { id } = req.params;
    if (productos[id - 1]) {
      productos[id - 1] = req.body;
      return res.status(200).json({
        message: "Prodcto ",
        content: productos[id - 1],
      });
    } else {
      return res.status(400).json({
        message: "Producto nno existe",
        content: null,
      });
    }
  })
  .delete((req, res) => {
    const { id } = req.params;
    if (productos[id - 1]) {
      const producto = productos[id - 1];
      productos.slice(id - 1, 1);

      return res.status(200).json({
        message: "producto eliminado",
        content: producto,
      });
    } else {
      return res.status(400).json({
        message: "Producto no existe",
        content: null,
      });
    }
  });

app.listen(PORT, () => console.log(`Ejecutandose en http://localhost:${PORT}`));
