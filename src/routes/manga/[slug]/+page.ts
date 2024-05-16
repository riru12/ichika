export const load = async ({ params }) => {

    let chapters: any = [];
    let data: any = {};
    
    async function fetchChapters(){
        const response = await fetch(`http://localhost:3000/sub_folders/${params.slug}`);
        data = await response.json();
        return data.folders;
    }
    chapters = await fetchChapters(); // Wait for chapters to be fetched

    return {
        slug: params.slug,
        chapters: chapters
    }
}   