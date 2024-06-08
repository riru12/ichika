<script lang="ts">
    import { onMount } from 'svelte';
    export let data;

    function createGenreItem(genreValue: string) {
        const genreList = document.getElementById('genre-list');
        const genreItemWrapper = document.createElement('div');
        genreItemWrapper.classList.add('flex', 'flex-row', 'bg-neutral-600', 'px-1', 'py-1', 'rounded-xl');

        const genreItem = document.createElement('input');
        genreItem.classList.add('text-sm', 'bg-neutral-600', 'text-neutral-300', 'text-center', 'pointer-events-none');
        genreItem.type = "text";
        genreItem.size = genreValue.length + 2;
        genreItem.value = genreValue;
        genreItem.name = "genres[]";
        genreItem.readOnly = true;

        const genreDel = document.createElement('button');
        genreDel.innerHTML = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='currentColor' class='size-4'><path d='M5.28 4.22a.75.75 0 0 0-1.06 1.06L6.94 8l-2.72 2.72a.75.75 0 1 0 1.06 1.06L8 9.06l2.72 2.72a.75.75 0 1 0 1.06-1.06L9.06 8l2.72-2.72a.75.75 0 0 0-1.06-1.06L8 6.94 5.28 4.22Z' /></svg>";
        genreDel.onclick = function () {
            genreList?.removeChild(genreItemWrapper);
        };

        genreItemWrapper.appendChild(genreItem);
        genreItemWrapper.appendChild(genreDel);
        genreList?.appendChild(genreItemWrapper);
    }

    function genreHandler() {
        const genreInput = document.getElementById('genre-input') as HTMLInputElement;
        const inp = genreInput?.value;
        if (inp) {
            createGenreItem(inp);
            genreInput.value = '';
        }
    }

    onMount(() => {
        const titleInput = document.getElementById('title') as HTMLInputElement;
        const authorInput = document.getElementById('author') as HTMLInputElement;
        const statusInput = document.getElementById('status') as HTMLSelectElement;
        const descInput = document.getElementById('desc') as HTMLInputElement;

        titleInput.value = data.manga.title;
        authorInput.value = data.manga.author;
        statusInput.value = data.manga.status;
        descInput.value = data.manga.desc;

        data.manga.genres.forEach((genre: string) => {
            createGenreItem(genre);
        });
    });
</script>

<section class="mx-12 md:mx-24 xl:mx-60 2xl:mx-96 py-8">
    <form action={`http://localhost:3000/api/manga/${data.manga._id}/update?_method=PUT`} method="post" id="update-manga">
        <div class="flex flex-col gap-4">
            <div class="flex flex-row gap-4 w-full flex-wrap">
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="title" class="text-sm ml-2">Title</label>
                    <input type="text" id="title" name="title" placeholder="Chainsaw Man" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white placeholder:text-neutral-600 ">
                </div>
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="author" class="text-sm ml-2">Author</label>
                    <input type="text" id="author" name="author" placeholder="Tatsuki Fujimoto" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white placeholder:text-neutral-600">
                </div>
                <div class="flex flex-col gap-1 flex-grow">
                    <label for="status" class="text-sm ml-2">Status</label>
                    <select id="status" name="status" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white">
                        <option value="Ongoing">Ongoing</option>
                        <option value="Completed">Completed</option>
                    </select>
                </div>
            </div>
            <div class="flex flex-col">
                <label for="genres" class="text-sm ml-2">Genres</label>
                <div id="genre-list" class="flex flex-row items-center gap-2 flex-wrap">
                    <input id="genre-input" type="text" placeholder="Enter a genre" class="rounded-3xl px-4 py-1 bg-[#13131a] text-white placeholder:text-neutral-600 w-min">
                    <button on:click={genreHandler} type="button">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                            <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 9a.75.75 0 0 0-1.5 0v2.25H9a.75.75 0 0 0 0 1.5h2.25V15a.75.75 0 0 0 1.5 0v-2.25H15a.75.75 0 0 0 0-1.5h-2.25V9Z" clip-rule="evenodd" />
                        </svg>
                    </button>
                </div>
            </div>
            <div>
                <label for="desc" class="text-sm ml-2">Description</label>
                <textarea id="desc" name="desc" class="w-full rounded-3xl px-4 py-1 bg-[#13131a] text-white h-36 resize-none"></textarea>
            </div>
            <!-- <div class="flex flex-row gap-4">
                <label for="cover">Update the cover photo:</label>
                <input type="file" id="cover" name="cover" accept="image/png, image/jpeg" class="file:px-4 file:bg-neutral-400 file:text-black file:rounded-3xl file:cursor-pointer hover:file:brightness-125"/>
            </div> -->
            <div class="flex justify-end">
                <button type="submit" form="update-manga" value="Submit" class="px-4 py-1 bg-indigo-700 text-white rounded-3xl hover:brightness-125">Submit</button>
            </div>
        </div>
    </form>
</section>
