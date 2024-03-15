return {
	"voldikss/vim-floaterm",
	config = function()
    vim.keymap.set("n", "<leader>fn", ":FloatermNew pwsh<ENTER>", {})
	end,
}
