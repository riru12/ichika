export const load = async ({ fetch }) => {
    async function fetchMangaList(){
        const response = await fetch(`http://localhost:3000/root_folders`);
        const data = await response.json();
        return data.folders;
    }

    return {
        mangaList: await fetchMangaList()
    }
}   