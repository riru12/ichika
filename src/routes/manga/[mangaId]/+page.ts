export const load = async ({ params, fetch }) => {
    async function fetchChapters( id:string ){
        const response = await fetch(`http://localhost:3000/sub_folders/${id}`);
        const data = await response.json();
        return data.folders;
    }

    return {
        mangaId: params.mangaId,
        chapters: await fetchChapters(params.mangaId)
    }
}   