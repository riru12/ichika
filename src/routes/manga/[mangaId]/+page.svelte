<script lang="ts">
    import { CldImage } from 'svelte-cloudinary';

    export let data;

    function deleteManga(id: string) {
        var result = confirm("Delete this manga? This action is irreversible.");
        if (result) {
            fetch(`http://localhost:3000/api/manga/${id}`, {method: 'DELETE',})
        }
    }
</script>


<section class="flex flex-col items-center mt-8 gap-8">
    <div class="flex md:flex-row flex-col w-3/4 2xl:w-1/2 md:gap-6 gap-4">
        <div class="aspect-[5/7.5] md:flex-shrink-0">
            <CldImage width="500" height="750" src={`${data.manga._id}/${data.manga.coverImg}`} alt={`${data.manga.title} Cover`} class="rounded"/>
        </div>
        <div class="flex flex-col justify-around gap-8">
            <div>
                <h2 class="text-3xl font-bold text-white">{data.manga.title}</h2>
                <h1 class="text-neutral-600">{data.manga.author}</h1>
                <p class="mt-2">{data.manga.desc}</p>
                <div class="flex flex-row gap-2 mt-2 flex-wrap">
                    {#each data.manga.genres as genres}
                        <p class="text-sm bg-neutral-800 px-3 py-1 rounded-xl">{genres}</p>
                    {/each}
                </div>
            </div>
            <div class="flex flex-row gap-2 flex-wrap">
                <a href={`/`} class="w-min md:basis-0 basis-full whitespace-nowrap bg-indigo-700 px-4 py-2 rounded-xl flex flex-row gap-2 items-center justify-center hover:brightness-125">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="white" class="w-5 h-5">
                        <path d="M7.25 3.688a8.035 8.035 0 0 0-4.872-.523A.48.48 0 0 0 2 3.64v7.994c0 .345.342.588.679.512a6.02 6.02 0 0 1 4.571.81V3.688ZM8.75 12.956a6.02 6.02 0 0 1 4.571-.81c.337.075.679-.167.679-.512V3.64a.48.48 0 0 0-.378-.475 8.034 8.034 0 0 0-4.872.523v9.268Z" />
                    </svg>
                    <span class="text-white">Start Reading</span>
                </a>
                <a href={`/manga/${data.manga._id}/update`} class="w-min md:basis-0 basis-full whitespace-nowrap bg-neutral-700 px-4 py-2 rounded-xl flex flex-row gap-2 items-center justify-center hover:brightness-125">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="white" class="size-4">
                        <path fill-rule="evenodd" d="M13.836 2.477a.75.75 0 0 1 .75.75v3.182a.75.75 0 0 1-.75.75h-3.182a.75.75 0 0 1 0-1.5h1.37l-.84-.841a4.5 4.5 0 0 0-7.08.932.75.75 0 0 1-1.3-.75 6 6 0 0 1 9.44-1.242l.842.84V3.227a.75.75 0 0 1 .75-.75Zm-.911 7.5A.75.75 0 0 1 13.199 11a6 6 0 0 1-9.44 1.241l-.84-.84v1.371a.75.75 0 0 1-1.5 0V9.591a.75.75 0 0 1 .75-.75H5.35a.75.75 0 0 1 0 1.5H3.98l.841.841a4.5 4.5 0 0 0 7.08-.932.75.75 0 0 1 1.025-.273Z" clip-rule="evenodd" />
                      </svg>                      
                    <span class="text-[#e6e6e6]">Update Manga</span>
                </a>
                <a on:click={() => deleteManga(data.manga._id)} href={`/manga`} class="w-min md:basis-0 basis-full whitespace-nowrap bg-[#330000] px-4 py-2 rounded-xl flex flex-row gap-2 items-center justify-center hover:brightness-125">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#e60000" class="size-6">
                        <path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 0 1 3.878.512.75.75 0 1 1-.256 1.478l-.209-.035-1.005 13.07a3 3 0 0 1-2.991 2.77H8.084a3 3 0 0 1-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 0 1-.256-1.478A48.567 48.567 0 0 1 7.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 0 1 3.369 0c1.603.051 2.815 1.387 2.815 2.951Zm-6.136-1.452a51.196 51.196 0 0 1 3.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 0 0-6 0v-.113c0-.794.609-1.428 1.364-1.452Zm-.355 5.945a.75.75 0 1 0-1.5.058l.347 9a.75.75 0 1 0 1.499-.058l-.346-9Zm5.48.058a.75.75 0 1 0-1.498-.058l-.347 9a.75.75 0 0 0 1.5.058l.345-9Z" clip-rule="evenodd" />
                    </svg>
                    <span class="text-[#ffcccc]">Delete Manga</span>
                </a>
            </div>
        </div>
    </div>
    <div class="w-3/4 2xl:w-1/2">
        <h2 class="text-white font-bold text-2xl">Chapters</h2>
        <div class="flex flex-col gap-1 mt-4">
            {#each data.manga.chapters as chapters}
                <p class="text-base bg-[#13131a] text-white font-bold px-3 py-1 rounded">{`Ch. ${chapters}`}</p>
            {/each}
        </div>
    </div>

</section>