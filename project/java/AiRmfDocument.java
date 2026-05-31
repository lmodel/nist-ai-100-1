package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Publication metadata for an instance of the AI RMF (e.g., NIST
AI 100-1, January 2023). The Framework is intended to be a
living document, employing a two-number versioning system (major.minor).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfDocument extends NamedThing {

  private String version;
  private String publisher;
  private URI doi;
  private LocalDate publishedDate;
  private URI source;


}