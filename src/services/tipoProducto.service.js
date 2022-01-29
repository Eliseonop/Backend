import { prisma } from "../prisma.js";

export class TipoProductoService {
  // los metodos estaticos son metodos que sirven para utilizarce sin hacer una instacion
  //y de la misma manera cuando se realñice la instacioa no se podra acceder a dicho metodo, estos metodos se usanma que todo para clases abstractas en la cual se usa pra plastillas para heremcia de otras clases
  static async crearTipoProducto({ nombreProducto, usuarioId }) {
    const usuarioEncontrado = await prisma.usuario.findUnique({
      where: { id: usuarioId },
    });
    console.log(usuarioEncontrado);
    return { message: "ok" };
  }
}
