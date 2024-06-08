export const load = async ({ params, fetch }) => {
    async function fetchChapters( id:string ){
        const response = await fetch(`http://localhost:3000/api/manga/${id}`);
        const data = await response.json();
        return data.manga
    }

    return {
        manga: await fetchChapters(params.mangaId)
    }
}