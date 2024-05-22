export const load = async ({ fetch }) => {
    async function fetchMangaList(){
        const response = await fetch(`http://localhost:3000/api/manga`);
        const data = await response.json();
        return data;
    }

    return {
        mangaList: await fetchMangaList()
    }
}   