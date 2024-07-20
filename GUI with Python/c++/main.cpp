#include <windows.h>
#include <commctrl.h> // For common controls (ttk)
#include <string>
#include <sstream>
#include <vector>
#include <functional>

// Function to set DPI awareness (adapt based on your requirements)
void dpi_awareness() {
    // Example using SetProcessDpiAwarenessContext
    SetProcessDpiAwarenessContext(DPI_AWARENESS_PER_MONITOR);
}

// Custom window class for the main application window
class DistanceConverterWindow : public HWND {
public:
    DistanceConverterWindow(const HINSTANCE& hInstance);
    ~DistanceConverterWindow();

    // Message handler for window creation and messages
    LRESULT CALLBACK WindowProc(UINT uMsg, WPARAM wParam, LPARAM lParam);

private:
    // Helper functions for creating UI elements and handling conversions
    HWND CreateLabel(const std::wstring& text, int x, int y, int width, int height);
    HWND CreateEntry(const std::wstring& text, int x, int y, int width, int height, HWND parent);
    void OnMetresChanged(HWND);
    void OnFeetChanged(HWND);

    // UI element handles
    HWND mainFrame;
    HWND metresLabel;
    HWND metresEntry;
    HWND feetLabel;
    HWND feetEntry;

    // Data members
    std::wstring metresValue;
    std::wstring feetValue;
};

DistanceConverterWindow::DistanceConverterWindow(const HINSTANCE& hInstance) {
    // Register window class (adapt based on your window style)
    WNDCLASSEX wc = { sizeof(WNDCLASSEX), CS_HREDRAW | CS_VREDRAW, WindowProc, 0, 0,
                      hInstance, LoadCursor(nullptr, IDC_ARROW), nullptr, nullptr, L"DistanceConverter" };
    RegisterClassEx(&wc);

    // Get screen dimensions
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);

    // Calculate window position
    int windowWidth = 600;
    int windowHeight = 300;
    int centerX = (screenWidth - windowWidth) / 2;
    int centerY = (screenHeight - windowHeight) / 2;

    // Create the window
    CREATESTRUCT cs = { 0 };
    cs.lpszClass = L"DistanceConverter";
    cs.style = WS_OVERLAPPEDWINDOW;
    cs.x = centerX;
    cs.y = centerY;
    cs.cx = windowWidth;
    cs.cy = windowHeight;
    CreateWindowEx(0, cs.lpszClass, L"Distance Converter", cs.style, cs.x, cs.y, cs.cx, cs.cy, nullptr, nullptr, hInstance, this);

    // Set the font for all child elements
    NONCLIENTMETRICS ncm;
    ncm.cbSize = sizeof(ncm);
    SystemParametersInfo(SPI_GETNONCLIENTMETRICS, sizeof(ncm), &ncm, 0);
    HFONT font = CreateFontPoint(13, ncm.lfHeight, ncm.lfWeight, ncm.lfItalic, ncm.lfUnderline, ncm.lfStrikeOut, ncm.lfCharSet,
                               OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_SWISS, ncm.lfFaceName);
    SendMessage(GetSafeHwnd(), WM_SETFONT, (WPARAM)font, 0);

    // Initialize data members
    metresValue = L"";
    feetValue = L"";

    ShowWindow(GetSafeHwnd(), SW_SHOW);
    UpdateWindow(GetSafeHwnd());
}

DistanceConverterWindow::~DistanceConverterWindow() {
    DestroyWindow(GetSafeHwnd());
}

LRESULT CALLBACK DistanceConverterWindow::WindowProc(UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CREATE: {
            // Create UI elements on window creation
            mainFrame = CreateWindowEx(0, L"STATIC", L"", WS_CHILD | WS_VISIBLE, 0, 0, 600, 300, GetSafeHwnd(), nullptr, GetModuleHandle(nullptr), nullptr);
            metres
