<script>
	import "../app.css";

	import AccountIcon from "./navIcons/AccountIcon.svelte";
    import HamburgerIcon from "./navIcons/HamburgerIcon.svelte";
	import HomeIcon from "./navIcons/HomeIcon.svelte";
	import BookIcon from "./navIcons/BookIcon.svelte";

	let mobileNav = 0;
	function mobileNavToggle(){
		mobileNav = 1-mobileNav;
	}
</script>

<div class="w-full z-50">
	<nav class="flex flex-row bg-[#2a2a2a] text-neutral-300 flex-grow justify-between px-8 md:px-24">
		<div class="flex">
			<div class="flex text-3xl text-white font-bold items-center px-6 py-2 whitespace-nowrap">一華</div>
			<div class="hidden md:flex items-center">
				<a class="hover:text-white px-6" href="/">Home</a>
				<a class="hover:text-white px-6" href="/manga">Manga</a>
			</div>
		</div>
		<div class="flex items-center">
			<a class="px-6 cursor-pointer" href="/account"><AccountIcon /></a>
			<button on:click={mobileNavToggle}><div class="flex md:hidden"><HamburgerIcon /></div></button>
		</div>
	</nav>
</div>
{#if mobileNav==1}
<div class="absolute w-fit right-8 translate-y-2 z-50 sm:hidden">
	<nav class="flex flex-col bg-[#2a2a2a] text-neutral-300 rounded-2xl gap-1 p-2">
		<a on:click={mobileNavToggle} class="px-12 py-2 text-lg hover:bg-[#444444d9] rounded-xl text-center" href="/"><div class="flex flex-row gap-2 items-center"><HomeIcon/>Home</div></a>
		<a on:click={mobileNavToggle} class="px-12 py-2 text-lg hover:bg-[#444444d9] rounded-xl text-center" href="/manga"><div class="flex flex-row gap-2 items-center"><BookIcon/>Manga</div></a>
	</nav>
</div>
<div on:click={mobileNavToggle} class="absolute bg-black w-screen h-screen opacity-40 sm:hidden z-30" role="none" />
{/if}

<slot />