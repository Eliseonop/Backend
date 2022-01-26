import { Prisma } from "../prisma.js";
import { categoriaRouter } from "../routes/categoria.routes.js";

export const crearCategoria = async (req, res) => {
  // req.body =>{ nombre:'lacteos'}
  const data = req.body;
  const content = await Prisma.categoria.create({ data });
  return res.json({ content });
};

export const listaCategoria = async (req, res) => {
  const categorias = await Prisma.categoria.findMany({});
  return res.json({ content: categorias });
};

export const buscarCategoria = async (req, res) => {
  console.log(req.query["estado"]);
  // si en los params hay el estado entonces validar antes de pasar a prisma que si su valor es 'true' entonces sera true caso contrario sera
  const params = req.query;
  if (params.estado) {
    params.estado = params.estado === "true" ? true : false;
  }
  const categorias = await Prisma.categoria.findMany({
    // where: { nombre: { mode: "insensitive", contains: "LACTEOS" } },
    where: { OR: [{ estado: false }, { nombre: "Lacteos" }] },
  });
  return res.json({
    content: categorias,
  });
};

export const actualizarCategoria = async (req, res) => {
  const  id  = +req.params.id;
  try {
    await Prisma.categoria.findUnique({ where: { id: id } });
    const categoriaActualizada = await Prisma.categoria.update({ 
      data: req.body, 
      where: { id } });

    return res.status(201).json({
      content: categoriaActualizada
    })
  } catch (error) {
    console.log(error);
    return res.status(400).json({
      message: "Error al actualizar la categoria"
    })
  } 
};
