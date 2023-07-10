fn main() {
    #[cfg(windows)]
    {
        let mut res = winres::WindowsResource::new();
        res.set_icon("assets\\images\\logo.ico");
        res.compile().unwrap();
    }
}
